import os
import shutil
import tempfile
from code_to_image import code_to_image # Import the function

TAB_WIDTH = 4

def _create_snapshot_ready_copy(input_file_path):
    with open(input_file_path, "r", encoding="ISO-8859-1") as source_file:
        text = source_file.read()

    normalized_text = text.expandtabs(TAB_WIDTH).replace("\r\n", "\n").replace("\r", "\n")

    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="ISO-8859-1",
        suffix=".txt",
        delete=False,
    ) as temp_file:
        temp_file.write(normalized_text)
        return temp_file.name

def process_text_files_and_generate_screenshots(input_base_dir, output_base_dir):
    try:
        # Ensure the output base directory exists and is empty
        if os.path.exists(output_base_dir):
            shutil.rmtree(output_base_dir)
        os.makedirs(output_base_dir)

        for root, dirs, files in os.walk(input_base_dir):
            # Construct the corresponding output directory path
            relative_path = os.path.relpath(root, input_base_dir)
            current_output_dir = os.path.join(output_base_dir, relative_path)

            # Create the mirrored directory in the output structure
            if not os.path.exists(current_output_dir):
                os.makedirs(current_output_dir)

            for file in files:
                if file.endswith(".txt"):
                    input_file_path = os.path.join(root, file)
                    # Create an output image filename based on the text file name
                    output_image_filename = os.path.splitext(file)[0] + ".png"
                    output_image_path = os.path.join(current_output_dir, output_image_filename)

                    print(f"Processing {input_file_path} -> {output_image_path}")
                    
                    normalized_input_file = _create_snapshot_ready_copy(input_file_path)
                    try:
                        # Render a normalized copy so tabs don't appear as visible glyphs.
                        code_to_image(filename=normalized_input_file, output_image=output_image_path)
                    finally:
                        if os.path.exists(normalized_input_file):
                            os.remove(normalized_input_file)

                    print(f"Successfully generated image for {file}")

        print("All text files processed and images generated.")

    except FileNotFoundError:
        print(f"Error: The input directory '{input_base_dir}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Assuming script is run from the BTP directory
    input_folder = "../Text_Files"
    output_folder = "../snapshots"
    process_text_files_and_generate_screenshots(input_folder, output_folder)
