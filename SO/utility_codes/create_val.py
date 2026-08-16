import os
import shutil
import random
from pathlib import Path

def create_test_set():
    # Define paths
    train_dir = Path("snapshots/Train")
    test_dir = Path("snapshots/Test")
    
    # Check if Train directory exists
    if not train_dir.exists():
        print(f"Error: Train directory '{train_dir}' not found.")
        return
    
    # Create Test directory structure
    test_dir.mkdir(exist_ok=True)
    
    # Process each label folder (Label_0 and Label_1)
    for label in ["Label_0", "Label_1"]:
        train_label_dir = train_dir / label
        test_label_dir = test_dir / label
        
        # Check if the label folder exists in Train
        if not train_label_dir.exists():
            print(f"Warning: Label folder '{label}' not found in Train directory. Skipping.")
            continue
        
        # Get all files in the train label directory (excluding subdirectories)
        all_files = [f for f in train_label_dir.iterdir() if f.is_file()]
        
        if not all_files:
            print(f"Warning: No files found in '{train_label_dir}'. Skipping.")
            continue
        
        # Calculate 20% of files (at least 1 file if directory is small)
        num_files_to_move = max(1, int(len(all_files) * 0.2))
        print(f"Moving {num_files_to_move} files (20%) from {label}")
        
        # Randomly select files to move
        files_to_move = random.sample(all_files, num_files_to_move)
        
        # Create the corresponding label directory in Test
        test_label_dir.mkdir(exist_ok=True)
        
        # Move the selected files
        moved_count = 0
        for file_path in files_to_move:
            try:
                target_path = test_label_dir / file_path.name
                shutil.move(str(file_path), str(target_path))
                moved_count += 1
            except Exception as e:
                print(f"Error moving file '{file_path.name}': {e}")
        
        print(f"Moved {moved_count}/{num_files_to_move} files from {label}")

    print("Test set creation completed!")

if __name__ == "__main__":
    create_test_set()