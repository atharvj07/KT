import os
import pandas as pd

# ---------- Configuration ----------
CSV_FOLDER = "../csvs"     # Folder containing .csv files
OUTPUT_BASE = "../text_files" # Where folders & text files will be created
CODE_COLUMN = "code"
LABEL_COLUMN = "label"
# ------------------------------------

os.makedirs(OUTPUT_BASE, exist_ok=True)

# Process each CSV file in the folder
for csv_file in os.listdir(CSV_FOLDER):
    if not csv_file.endswith(".csv"):
        continue

    csv_path = os.path.join(CSV_FOLDER, csv_file)
    df = pd.read_csv(csv_path)

    # Create a base folder for this CSV file (without .csv extension)
    csv_name = os.path.splitext(csv_file)[0]
    csv_output_dir = os.path.join(OUTPUT_BASE, csv_name)
    os.makedirs(csv_output_dir, exist_ok=True)

    # Ensure columns exist
    if CODE_COLUMN not in df.columns or LABEL_COLUMN not in df.columns:
        print(f"⚠️ Skipping {csv_file}: missing '{CODE_COLUMN}' or '{LABEL_COLUMN}' column")
        continue

    # Create label folders and text files
    for idx, row in df.iterrows():
        label = row[LABEL_COLUMN]
        code_text = str(row[CODE_COLUMN])

        label_dir = os.path.join(csv_output_dir, f"Label_{label}")
        os.makedirs(label_dir, exist_ok=True)

        # Save code as text file
        out_path = os.path.join(label_dir, f"sample_{idx}.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(code_text)

    print(f"✅ Processed {csv_file} → {csv_output_dir}")