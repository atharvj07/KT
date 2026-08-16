import numpy as np
import os
import argparse
from typing import Tuple
import sys
import torch
from torch.utils.data import Dataset
import random
import pandas as pd
import csv

# Argument parsing
parser = argparse.ArgumentParser()                                                        
parser.add_argument('--cache_dir', type=str, default="./cache")
parser.add_argument('--set_threshold', type=int, default=470)
parser.add_argument('--languages', type=list, default=['Java','C++','Python','JavaScript','C#','C','Go','Ruby','Rust','Kotlin'])
parser.add_argument('--random_seed', type=int, default=36)
parser.add_argument('--name_trainer', type=str, default="trainer")
parser.add_argument('--local_dataset', type=bool, default=True)
parser.add_argument('--path_to_dataset', type=str, default="./H-AIRosettaMP.csv")
parser.add_argument('--output_dir', type=str, default="./multilingual_data")

args = parser.parse_args()

languages = args.languages
local_dataset = args.local_dataset
path_to_dataset = args.path_to_dataset
threshold = args.set_threshold
cache_dir = args.cache_dir
random_seed = args.random_seed
output_dir = args.output_dir

os.environ["HF_HOME"] = cache_dir
os.environ["HF_HUB_CACHE"] = cache_dir
os.environ["HF_ASSETS_CACHE"] = cache_dir
os.environ["HF_TOKEN"] = cache_dir
os.environ["HF_DATASETS_CACHE"] = cache_dir
import datasets
import transformers

def data_splitter_preserve_pairs(dataset: pd.DataFrame, gen: torch.Generator, lan: str):
    """Split data while preserving AI-Human task pairs"""
    # Get unique tasks
    unique_tasks = dataset['task_name'].unique()
    print(f"Total unique tasks for {lan}: {len(unique_tasks)}")
    
    # Shuffle tasks (not individual samples)
    task_indices = torch.randperm(len(unique_tasks), generator=gen)
    
    # Split tasks 80-20
    split_point = int(len(unique_tasks) * 0.80)
    train_tasks = unique_tasks[task_indices[:split_point]]
    val_tasks = unique_tasks[task_indices[split_point:]]
    
    # Get all samples for train tasks and val tasks
    train_data = dataset[dataset['task_name'].isin(train_tasks)]
    val_data = dataset[dataset['task_name'].isin(val_tasks)]
    
    print(f"After split - {lan}: {len(train_data)} train samples, {len(val_data)} validation samples")
    print(f"Train tasks: {len(train_tasks)}, Validation tasks: {len(val_tasks)}")
    
    return train_data, val_data

def fix_random(seed: int = 42) -> None:
    transformers.set_seed(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True
    gen_loader = torch.Generator()
    gen_loader.manual_seed(seed)
    return gen_loader

def intra_language_balancing(intra_language_set, bound, current_lan, languages):
    num_lan = len(languages) - 1
    intra_language_set_AI = intra_language_set[intra_language_set["target"] == "Ai_generated"]
    intra_language_set_Human = intra_language_set[intra_language_set["target"] == "Human_written"]
    intra_language_set_AI = intra_language_set_AI.reset_index(drop=False)
    intra_language_set_Human = intra_language_set_Human.reset_index(drop=False)

    my_balanced_subset_AI = pd.DataFrame(columns=intra_language_set_AI.columns)
    my_balanced_subset_Human = pd.DataFrame(columns=intra_language_set_Human.columns)

    rdn = torch.randperm(len(intra_language_set_Human))
    languages.remove(current_lan)
    sampler = torch.distributions.categorical.Categorical(torch.tensor([0.11, 0.11, 0.11, 0.11, 0.11, 0.11, 0.11, 0.11, 0.11]))

    reference_dict = dict(zip(range(num_lan), languages))
    multiple_sets_split = {}
    for lan in languages:
        multiple_sets_split[lan] = (intra_language_set_AI[intra_language_set_AI["set"] == f"{current_lan}_from_{lan}"], list(torch.randperm(len(intra_language_set_AI[intra_language_set_AI["set"] == f"{current_lan}_from_{lan}"]))))

    idx = 0
    while len(my_balanced_subset_AI) < bound:
        sampled_language = reference_dict[int(sampler.sample())]
        element = multiple_sets_split[sampled_language][0].iloc[int(multiple_sets_split[sampled_language][1].pop(0))]
        element = element.to_frame().T
        idx += 1
        if len(my_balanced_subset_AI) > 0 and not(element['task_name'].values[0] in my_balanced_subset_AI['task_name'].values) and element['task_name'].values[0] in intra_language_set_Human['task_name'].values:
            my_balanced_subset_AI = pd.concat([my_balanced_subset_AI, element], ignore_index=True)  
        if len(my_balanced_subset_AI) == 0 and element['task_name'].values[0] in intra_language_set_Human['task_name'].values:
            my_balanced_subset_AI = element

    idx = 0
    while len(my_balanced_subset_Human) < bound:
        try:
            element = intra_language_set_Human.iloc[int(rdn[idx])]
            element = element.to_frame().T
            idx += 1

            if len(my_balanced_subset_Human) > 0 and not(element['task_name'].values[0] in my_balanced_subset_Human['task_name'].values) and element['task_name'].values[0] in my_balanced_subset_AI['task_name'].values:
                my_balanced_subset_Human = pd.concat([my_balanced_subset_Human, element], ignore_index=True)   
            if len(my_balanced_subset_Human) == 0 and element['task_name'].values[0] in my_balanced_subset_AI['task_name'].values:
                my_balanced_subset_Human = element 
        except IndexError:
            print("INDEX ERROR")
            idx = 0
            while len(my_balanced_subset_Human) < bound:
                element = intra_language_set_Human.iloc[int(rdn[-idx])]
                element = element.to_frame().T
                my_balanced_subset_Human = pd.concat([my_balanced_subset_Human, element], ignore_index=True)   

    my_balanced_subset = pd.concat([my_balanced_subset_AI, my_balanced_subset_Human], ignore_index=True)
    print(f"Balanced subset for {current_lan}: {len(my_balanced_subset)} elements (AI: {len(my_balanced_subset_AI)}, Human: {len(my_balanced_subset_Human)})")

    return my_balanced_subset

def verify_task_pairing(dataset: pd.DataFrame, dataset_name: str):
    """Verify that each task has exactly 2 files (1 AI + 1 Human)"""
    task_counts = dataset.groupby('task_name')['target'].nunique()
    tasks_with_one_file = task_counts[task_counts == 1]
    tasks_with_more_than_two = task_counts[task_counts > 2]
    
    print(f"\n--- {dataset_name} Task Pairing Verification ---")
    print(f"Total tasks: {len(task_counts)}")
    print(f"Tasks with only 1 file: {len(tasks_with_one_file)}")
    print(f"Tasks with more than 2 files: {len(tasks_with_more_than_two)}")
    
    if len(tasks_with_one_file) > 0:
        print("WARNING: Some tasks have only one file (missing AI/Human pair):")
        for task in tasks_with_one_file.index[:5]:  # Show first 5
            task_data = dataset[dataset['task_name'] == task]
            targets = task_data['target'].values
            print(f"  Task {task}: {len(task_data)} files - {targets}")
    
    if len(tasks_with_more_than_two) > 0:
        print("WARNING: Some tasks have more than 2 files:")
        for task in tasks_with_more_than_two.index[:5]:  # Show first 5
            task_data = dataset[dataset['task_name'] == task]
            targets = task_data['target'].values
            print(f"  Task {task}: {len(task_data)} files - {targets}")
    
    # Check perfect pairing
    perfect_pairs = task_counts[task_counts == 2]
    print(f"Tasks with perfect pairing (2 files): {len(perfect_pairs)}")
    
    # Additional check: verify each task has exactly 1 AI and 1 Human
    task_composition = dataset.groupby('task_name')['target'].value_counts()
    incomplete_pairs = []
    for task in task_counts.index:
        if task_counts[task] == 2:
            composition = task_composition[task]
            if len(composition) != 2 or not ('Ai_generated' in composition.index and 'Human_written' in composition.index):
                incomplete_pairs.append(task)
    
    if incomplete_pairs:
        print(f"Tasks with 2 files but incorrect composition: {len(incomplete_pairs)}")
        for task in incomplete_pairs[:3]:
            print(f"  {task}: {task_composition[task].to_dict()}")
    
    return len(tasks_with_one_file) == 0 and len(tasks_with_more_than_two) == 0 and len(incomplete_pairs) == 0

def save_datasets(output_dir: str, train_datasets: dict, val_datasets: dict, multilingual_train: pd.DataFrame, multilingual_val: pd.DataFrame):
    """Save all processed datasets to files"""
    
    # Create output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Verify task pairing before saving
    all_good = True
    
    print("\n=== VERIFYING TASK PAIRING ===")
    
    # Verify per-language datasets
    for lang, (train_df, val_df) in train_datasets.items():
        train_ok = verify_task_pairing(train_df, f"{lang} Training")
        val_ok = verify_task_pairing(val_df, f"{lang} Validation")
        if not (train_ok and val_ok):
            all_good = False
    
    # Verify multilingual datasets
    multi_train_ok = verify_task_pairing(multilingual_train, "Multilingual Training")
    multi_val_ok = verify_task_pairing(multilingual_val, "Multilingual Validation")
    if not (multi_train_ok and multi_val_ok):
        all_good = False
    
    if not all_good:
        print("\n⚠️  WARNING: Some datasets have incomplete task pairs!")
        response = input("Continue with saving? (y/n): ")
        if response.lower() != 'y':
            print("Aborting save operation.")
            return
    
    # Save per-language datasets
    for lang, (train_df, val_df) in train_datasets.items():
        lang_dir = os.path.join(output_dir, f"language_{lang}")
        if not os.path.exists(lang_dir):
            os.makedirs(lang_dir)
        
        # Save training data
        train_file = os.path.join(lang_dir, f"{lang}_train.csv")
        train_df.to_csv(train_file, index=False)
        print(f"Saved {lang} training data: {train_file} ({len(train_df)} samples)")
        
        # Save validation data
        val_file = os.path.join(lang_dir, f"{lang}_val.csv")
        val_df.to_csv(val_file, index=False)
        print(f"Saved {lang} validation data: {val_file} ({len(val_df)} samples)")
    
    # Save multilingual datasets
    multilingual_dir = os.path.join(output_dir, "multilingual")
    if not os.path.exists(multilingual_dir):
        os.makedirs(multilingual_dir)
    
    # Save multilingual training data
    multilingual_train_file = os.path.join(multilingual_dir, "multilingual_train.csv")
    multilingual_train.to_csv(multilingual_train_file, index=False)
    print(f"Saved multilingual training data: {multilingual_train_file} ({len(multilingual_train)} samples)")
    
    # Save multilingual validation data
    multilingual_val_file = os.path.join(multilingual_dir, "multilingual_val.csv")
    multilingual_val.to_csv(multilingual_val_file, index=False)
    print(f"Saved multilingual validation data: {multilingual_val_file} ({len(multilingual_val)} samples)")
    
    # Save dataset statistics
    stats_file = os.path.join(output_dir, "dataset_statistics.txt")
    with open(stats_file, 'w') as f:
        f.write("Multilingual Dataset Statistics\n")
        f.write("=" * 40 + "\n\n")
        
        f.write("Overall Multilingual Training Set:\n")
        f.write(f"  Total samples: {len(multilingual_train)}\n")
        f.write(f"  AI-generated: {len(multilingual_train[multilingual_train['target'] == 'Ai_generated'])}\n")
        f.write(f"  Human-written: {len(multilingual_train[multilingual_train['target'] == 'Human_written'])}\n")
        f.write(f"  Languages: {multilingual_train['language_name'].unique().tolist()}\n\n")
        
        f.write("Overall Multilingual Validation Set:\n")
        f.write(f"  Total samples: {len(multilingual_val)}\n")
        f.write(f"  AI-generated: {len(multilingual_val[multilingual_val['target'] == 'Ai_generated'])}\n")
        f.write(f"  Human-written: {len(multilingual_val[multilingual_val['target'] == 'Human_written'])}\n")
        f.write(f"  Languages: {multilingual_val['language_name'].unique().tolist()}\n\n")
        
        f.write("Per-language Statistics:\n")
        for lang in train_datasets.keys():
            train_lang_df = train_datasets[lang][0]
            val_lang_df = val_datasets[lang][1]
            
            train_ai_count = len(train_lang_df[train_lang_df['target'] == 'Ai_generated'])
            train_human_count = len(train_lang_df[train_lang_df['target'] == 'Human_written'])
            val_ai_count = len(val_lang_df[val_lang_df['target'] == 'Ai_generated'])
            val_human_count = len(val_lang_df[val_lang_df['target'] == 'Human_written'])
            
            f.write(f"\n{lang}:\n")
            f.write(f"  Training: {len(train_lang_df)} samples (AI: {train_ai_count}, Human: {train_human_count})\n")
            f.write(f"  Validation: {len(val_lang_df)} samples (AI: {val_ai_count}, Human: {val_human_count})\n")

def save_dataset_info(output_dir: str, languages: list, threshold: int, random_seed: int):
    """Save configuration information about the dataset processing"""
    info_file = os.path.join(output_dir, "dataset_info.csv")
    with open(info_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Parameter", "Value"])
        writer.writerow(["Languages", ", ".join(languages)])
        writer.writerow(["Samples per language", threshold])
        writer.writerow(["Random seed", random_seed])
        writer.writerow(["Processing date", pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")])

def get_dataset_language_name(lang: str) -> str:
    """Convert language name to the format used in the dataset"""
    return lang

def main():
    print("Starting multilingual data processing and saving...")
    
    # Create output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Fix random seed for reproducibility
    gen_loader = fix_random(seed=random_seed)
    
    # Load dataset
    if local_dataset:
        print(f"Loading dataset from local file: {path_to_dataset}")
        my_dataset = pd.read_csv(path_to_dataset)
    else:
        print("Dataset loading from HuggingFace would go here")
        return
    
    print(f"Loaded dataset with {len(my_dataset)} total samples")
    
    # Check what language names actually exist in the dataset
    actual_languages = my_dataset['language_name'].unique()
    print(f"Languages found in dataset: {actual_languages}")
    
    # Process data for each language
    cumulative_dataset = pd.DataFrame([])
    
    for lan_to_mine in languages:
        dataset_lang_name = get_dataset_language_name(lan_to_mine)
        print(f"\nProcessing language: {lan_to_mine} (dataset name: {dataset_lang_name})")
        unbalanced_language_set = pd.DataFrame([])
        
        # Collect data from all translation pairs for this language
        for lan_to_translate in languages:
            if lan_to_mine != lan_to_translate:
                dataset_translate_name = get_dataset_language_name(lan_to_translate)
                set_name = f"{dataset_lang_name}_from_{dataset_translate_name}"
                dataset_instance = my_dataset[my_dataset["set"] == set_name]
                print(f"  {set_name}: {len(dataset_instance)} samples")
                unbalanced_language_set = pd.concat([unbalanced_language_set, dataset_instance], ignore_index=True)
        
        if len(unbalanced_language_set) == 0:
            print(f"  WARNING: No data found for language {lan_to_mine}")
            continue
            
        # Balance the dataset for this language
        balanced_language_set = intra_language_balancing(unbalanced_language_set, threshold, lan_to_mine, languages.copy())
        cumulative_dataset = pd.concat([cumulative_dataset, balanced_language_set], ignore_index=True)
        
        print(f"Completed processing for {lan_to_mine}: {len(balanced_language_set)} balanced samples")
    
    print(f"\nTotal cumulative dataset size: {len(cumulative_dataset)} samples")
    
    # Verify the cumulative dataset has proper pairing
    print("\n=== VERIFYING CUMULATIVE DATASET ===")
    cumulative_ok = verify_task_pairing(cumulative_dataset, "Cumulative Dataset")
    if not cumulative_ok:
        print("WARNING: Cumulative dataset has pairing issues before splitting!")
    
    # Split data per language for multilingual training - PRESERVING PAIRS
    print("\n--Splitting dataset per language for multilingual training (preserving pairs)--")
    train_datasets = {}
    val_datasets = {}
    
    for lan in languages:
        dataset_lang_name = get_dataset_language_name(lan)
        # Filter dataset for current language using the correct dataset language name
        lang_data = cumulative_dataset[cumulative_dataset["language_name"] == dataset_lang_name]
        lang_data = lang_data.drop(columns=['__index_level_0__'], errors='ignore')
        
        if len(lang_data) > 0:
            # Use the new splitting function that preserves task pairs
            train_df, val_df = data_splitter_preserve_pairs(lang_data, gen=gen_loader, lan=lan)
            
            train_datasets[lan] = (train_df, train_df)
            val_datasets[lan] = (val_df, val_df)
            print(f"  {lan}: {len(train_df)} train samples, {len(val_df)} validation samples")
        else:
            print(f"  Warning: No data found for language {lan}")
    
    # Combine all languages for multilingual datasets
    print("\n--Creating combined multilingual datasets--")
    dataset_train = pd.DataFrame([])
    dataset_val = pd.DataFrame([])
    
    for lang in train_datasets.keys():
        train_df = train_datasets[lang][0]
        val_df = val_datasets[lang][1]
        dataset_train = pd.concat([dataset_train, train_df], ignore_index=True)
        dataset_val = pd.concat([dataset_val, val_df], ignore_index=True)
    
    print(f"Multilingual training set: {len(dataset_train)} samples")
    print(f"Multilingual validation set: {len(dataset_val)} samples")
    
    # Save all datasets
    print("\n--Saving processed datasets--")
    save_datasets(output_dir, train_datasets, val_datasets, dataset_train, dataset_val)
    save_dataset_info(output_dir, languages, threshold, random_seed)
    
    # Print final summary
    print("\n" + "="*60)
    print("DATA PROCESSING COMPLETED SUCCESSFULLY!")
    print("="*60)
    print(f"Output directory: {output_dir}")
    print(f"Total languages processed: {len(languages)}")
    print(f"Multilingual training samples: {len(dataset_train)}")
    print(f"Multilingual validation samples: {len(dataset_val)}")
    print(f"Per-language datasets saved in: {output_dir}/language_*/")
    print(f"Multilingual datasets saved in: {output_dir}/multilingual/")
    print("="*60)

if __name__ == '__main__':
    main()