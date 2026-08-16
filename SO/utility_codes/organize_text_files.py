import os
import pandas as pd
import shutil

def organize_files(base_text_path, base_csv_path):
    subfolders = [f.name for f in os.scandir(base_text_path) if f.is_dir()]

    for subfolder in subfolders:
        text_subfolder_path = os.path.join(base_text_path, subfolder)
        csv_file_path = os.path.join(base_csv_path, f"{subfolder}.csv")

        if not os.path.exists(csv_file_path):
            print(f"Warning: CSV file not found for {subfolder}. Skipping.")
            continue

        print(f"Processing folder: {subfolder}")

        df = pd.read_csv(csv_file_path)

        label_0_path = os.path.join(text_subfolder_path, "Label_0")
        label_1_path = os.path.join(text_subfolder_path, "Label_1")

        os.makedirs(label_0_path, exist_ok=True)
        os.makedirs(label_1_path, exist_ok=True)

        for index, row in df.iterrows():
            # Assuming file names are like 'generated_text_X.txt' where X is the index
            file_name = f"generated_text_{index}.txt"
            source_file_path = os.path.join(text_subfolder_path, file_name)
            label = row["label"]

            if os.path.exists(source_file_path):
                if label == 0:
                    destination_path = os.path.join(label_0_path, file_name)
                elif label == 1:
                    destination_path = os.path.join(label_1_path, file_name)
                else:
                    print(f"Unknown label {label} for file {file_name}. Skipping.")
                    continue
                shutil.move(source_file_path, destination_path)
            else:
                # Some folders (Java_Separate, Python_Separate) have the code in CSV directly, not as separate files
                # This part is a placeholder for handling those cases if needed, but for now we assume file existence.
                # If these folders don't have separate files and the CSV contains the full code,
                # we might need to create files from the 'Code' or 'clean_code' column.
                # For this task, I'll assume that the files exist for all subfolders in Text_Files
                # and are named 'generated_text_X.txt'.
                print(f"File {file_name} not found in {text_subfolder_path}. This might be expected for Java_Separate/Python_Separate if codes are directly in CSV.")


if __name__ == "__main__":
    base_text_path = "/home/info-sec-lab/BTP/Text_Files/Python_Separate"
    base_csv_path = "/home/info-sec-lab/BTP/CSVs/Python_Separate"
    organize_files(base_text_path, base_csv_path)
