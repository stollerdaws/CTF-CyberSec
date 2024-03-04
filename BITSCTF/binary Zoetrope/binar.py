from PIL import Image, ImageDraw
import os
from pathlib import Path

# Define the directory containing the binary data files
data_directory = Path("data")

# Set the dimensions of each frame in the GIF
frame_width = 320  # Width of the image 
frame_height = 240  # Height of the image

def create_image_from_binary(binary_data, width, height):
    image = Image.new('1', (width, height))  # '1' for 1-bit pixels, black and white
    draw = ImageDraw.Draw(image)

    # Draw the binary data as pixels on the image
    index = 0
    for y in range(height):
        for x in range(width):
            if index < len(binary_data):
                color = 255 if binary_data[index] == '1' else 0  # White for '1', black for '0'
                draw.point((x, y), fill=color)
                index += 1
    return image

def main():
    images = []
    for file_path in sorted(data_directory.glob('*.txt')):
        with open(file_path, 'r') as file:
            binary_data = file.read().strip().replace('\n', '')  # Remove newlines
            image = create_image_from_binary(binary_data, frame_width, frame_height)
            images.append(image)
    
    # Save the frames as an animated GIF
    output_filename = 'output.gif'
    images[0].save(output_filename, save_all=True, append_images=images[1:], optimize=False, loop=0, duration=100)
    print(f"Animated GIF created and saved as {output_filename}")

if __name__ == "__main__":
    main()
