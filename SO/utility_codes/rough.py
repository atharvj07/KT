import os
from PIL import Image

def is_image_valid(img_path):
    try:
        with Image.open(img_path) as img:
            img.verify()
        return True
    except Exception:
        print("KRSNA")
        return False

def is_text_valid(txt_path):
    try:
        with open(txt_path, 'r', encoding='utf-8') as f:
            f.read()
        return True
    except Exception:
        return False

def clean_corrupt_pairs(text_folder, image_folder):
    for label in ['Label_0', 'Label_1']:
        text_label_path = os.path.join(text_folder, label)
        image_label_path = os.path.join(image_folder, label)
        
        if not os.path.isdir(text_label_path) or not os.path.isdir(image_label_path):
            continue
        
        for txt_file in os.listdir(text_label_path):
            if not txt_file.lower().endswith('.txt'):
                continue
            
            txt_path = os.path.join(text_label_path, txt_file)
            base_name = os.path.splitext(txt_file)[0]

            # Try common image extensions
            img_path = None
            for ext in ['.jpg', '.jpeg', '.png']:
                candidate = os.path.join(image_label_path, base_name + ext)
                if os.path.exists(candidate):
                    img_path = candidate
                    break
            
            if img_path is None:
                print(f"No image found for {txt_path}, skipping...")
                continue
            

            # Delete if either is corrupt
            if not is_text_valid(txt_path) or not is_image_valid(img_path):
                print(f"Deleting corrupt pair: {txt_path} & {img_path}")
                os.remove(txt_path)
                os.remove(img_path)

# Usage
folder1 = r"Text_Files/Test_1"  # texts
folder2 = r"snapshots/Test_1"  # images

clean_corrupt_pairs(folder1, folder2)
