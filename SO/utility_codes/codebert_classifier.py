import os
import pandas as pd
from sklearn.model_selection import train_test_split
from transformers import RobertaTokenizer, RobertaForSequenceClassification, Trainer, TrainingArguments
import torch

# Configuration
MODEL_NAME = "microsoft/codebert-base"
NUM_LABELS = 2
BATCH_SIZE = 8
LEARNING_RATE = 2e-5
EPOCHS = 3

class CodeDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

def load_and_preprocess_data(base_path, tokenizer, folder_name):
    codes = []
    labels = []
    for label_dir in ["Label_0", "Label_1"]:
        current_path = os.path.join(base_path, folder_name, label_dir)
        if not os.path.exists(current_path):
            print(f"Warning: Directory {current_path} not found. Skipping.")
            continue
        for filename in os.listdir(current_path):
            if filename.endswith(".txt"):
                filepath = os.path.join(current_path, filename)
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    codes.append(f.read())
                labels.append(0 if label_dir == "Label_0" else 1)

    # Tokenize the codes
    encodings = tokenizer(codes, truncation=True, padding=True, max_length=512)
    return CodeDataset(encodings, labels)

def main():
    base_text_path = "/home/info-sec-lab/BTP/Text_Files"

    # Load tokenizer and model
    tokenizer = RobertaTokenizer.from_pretrained(MODEL_NAME)
    model = RobertaForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=NUM_LABELS)

    # Load and preprocess training data
    print("Loading training data...")
    train_dataset = load_and_preprocess_data(base_text_path, tokenizer, "Train")

    # Training arguments
    training_args = TrainingArguments(
        output_dir="./results",
        num_train_epochs=EPOCHS,
        per_device_train_batch_size=BATCH_SIZE,
        per_device_eval_batch_size=BATCH_SIZE,
        warmup_steps=500,
        weight_decay=0.01,
        logging_dir="./logs",
        logging_steps=10,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
        metric_for_best_model="accuracy",
    )

    # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
    )

    print("Training model...")
    trainer.train()

    # Evaluate on test datasets
    print("Evaluating on test datasets...")
    for i in range(10):
        test_folder = f"Test_{i}"
        print(f"Loading test data for {test_folder}...")
        test_dataset = load_and_preprocess_data(base_text_path, tokenizer, test_folder)
        if len(test_dataset) > 0:
            predictions = trainer.predict(test_dataset)
            # Process predictions to get labels
            predicted_labels = predictions.predictions.argmax(axis=1)
            true_labels = test_dataset.labels

            from sklearn.metrics import accuracy_score, precision_recall_fscore_support
            accuracy = accuracy_score(true_labels, predicted_labels)
            precision, recall, f1, _ = precision_recall_fscore_support(true_labels, predicted_labels, average='binary')

            print(f"Results for {test_folder}:")
            print(f"  Accuracy: {accuracy:.4f}")
            print(f"  Precision: {precision:.4f}")
            print(f"  Recall: {recall:.4f}")
            print(f"  F1-Score: {f1:.4f}")
        else:
            print(f"No data found for {test_folder}. Skipping evaluation.")

if __name__ == "__main__":
    main()

