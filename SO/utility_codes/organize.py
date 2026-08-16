import os
import pandas as pd
import shutil
from pathlib import Path

def organize_screenshots():
    # Define root paths
    l1 = ["snapshots/Python_Separate", "snapshots/Java_Separate", "snapshots"]
    l2 = ["CSVs/Python_Separate", "CSVs/Java_Separate", "CSVs"]
    # Define root paths
    for i in range(len(l1)):
        screenshots_root = Path(l1[i])
        csvs_root = Path(l2[i])
        
        # Check if necessary directories exist
        if not screenshots_root.exists():
            print(f"Error: Directory '{screenshots_root}' not found.")
            return
        if not csvs_root.exists():
            print(f"Error: Directory '{csvs_root}' not found.")
            return
        
        # Find all folders in Screenshots_Output that contain PNG files
        for folder_path in screenshots_root.rglob('*'):
            if folder_path.is_dir():
                png_files = list(folder_path.glob('*.png'))
                if not png_files:
                    continue  # Skip folders with no PNGs
                    
                print(f"Processing folder: {folder_path}")
                
                # Find corresponding CSV file
                # Assuming the CSV has the same name as the immediate parent folder of the PNGs
                csv_filename = folder_path.name + ".csv"
                csv_file_path = csvs_root / csv_filename
                
                if not csv_file_path.exists():
                    print(f"  Warning: Corresponding CSV file '{csv_filename}' not found in {csvs_root}. Skipping.")
                    continue
                    
                # Read the CSV file
                try:
                    df = pd.read_csv(csv_file_path)
                except Exception as e:
                    print(f"  Error reading CSV file '{csv_file_path}': {e}. Skipping.")
                    continue
                    
                # Check if 'label' column exists
                if 'label' not in df.columns:
                    print(f"  Error: 'label' column not found in '{csv_filename}'. Skipping.")
                    continue
                    
                # Create target subfolders for labels
                # We'll use generic names: Label_0 and Label_1
                # You can customize this logic if your labels are different
                label_0_dir = folder_path / "Label_0"
                label_1_dir = folder_path / "Label_1"
                label_0_dir.mkdir(exist_ok=True)
                label_1_dir.mkdir(exist_ok=True)
                
                moved_count = 0
                # Process each PNG file in the current folder
                for png_file in png_files:
                    # Extract the index from the filename (assuming format like 'image_123.png')
                    stem = png_file.stem  # gets 'image_123' from 'image_123.png'
                    
                    # Try to find the number at the end of the filename
                    try:
                        # Split by underscore and take the last part
                        index_str = stem.split('_')[-1]
                        file_index = int(index_str)
                    except (ValueError, IndexError):
                        print(f"  Warning: Could not extract index from filename '{png_file.name}'. Skipping.")
                        continue
                        
                    # Check if the index exists in the DataFrame
                    if file_index >= len(df):
                        print(f"  Warning: Index {file_index} from file '{png_file.name}' is out of bounds for CSV. Skipping.")
                        continue
                        
                    # Get the label for this index
                    label_value = df.iloc[file_index]['label']
                    
                    # Determine the target directory based on the label
                    if label_value == 0:
                        target_dir = label_0_dir
                    elif label_value == 1:
                        target_dir = label_1_dir
                    else:
                        print(f"  Warning: Unhandled label value '{label_value}' for file '{png_file.name}'. Skipping.")
                        continue
                        
                    # Move the file to the appropriate directory
                    target_path = target_dir / png_file.name
                    try:
                        shutil.move(str(png_file), str(target_path))
                        moved_count += 1
                    except Exception as e:
                        print(f"  Error moving file '{png_file.name}': {e}")
                        
                print(f"  Moved {moved_count} files for folder '{folder_path.name}'.")
            
    print("Organization complete!")

if __name__ == "__main__":
    organize_screenshots()