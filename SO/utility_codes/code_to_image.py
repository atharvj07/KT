from PIL import Image, ImageDraw, ImageFont
import os

# Define the font to use
font = ImageFont.load_default()

# Define the image dimensions
img_size = (399, 399)

# Loop through the text files in the input subdirectory and process each one
def code_to_image(filename, output_image):
    if filename.endswith(".txt"):
        # Read the contents of the text file
        with open(filename, "r", encoding="ISO-8859-1") as f:
            text = f.read()

        # Create a new image with the specified dimensions and black background
        img = Image.new("RGB", img_size, (0, 0, 0))

        # Draw the text onto the image with white color
        draw = ImageDraw.Draw(img)
        draw.text((0, 0), text, font=font, fill=(255, 255, 255))

        # Save the image to the output directory with the same name as the input text file
        img.save(output_image)