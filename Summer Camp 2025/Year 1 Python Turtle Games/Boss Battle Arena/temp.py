# resize_gif_by_width.py
# python temp.py FILEINPUT.gif FILEOUTPUT.gif WIDTH

# python temppy space1.gif space2.gif 1000
#python temp.py enemy.gif enemydy.gif 120

from PIL import Image, ImageSequence
import sys
import os

def resize_gif_by_width(input_path, output_path, new_width):
    with Image.open(input_path) as img:
        original_width, original_height = img.size
        aspect_ratio = original_height / original_width
        new_height = int(new_width * aspect_ratio)

        frames = []
        for frame in ImageSequence.Iterator(img):
            resized_frame = frame.copy().resize((new_width, new_height), Image.LANCZOS)
            frames.append(resized_frame.convert("P", palette=Image.ADAPTIVE))

        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            loop=img.info.get("loop", 0),
            duration=img.info.get("duration", 100),
            disposal=2,
            transparency=img.info.get("transparency", None)
        )

        print(f"Saved resized GIF to {output_path} ({new_width}x{new_height})")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python resize_gif_by_width.py <input.gif> <output.gif> <new_width>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    width = int(sys.argv[3])

    if not os.path.isfile(input_file):
        print("Error: input file does not exist.")
        sys.exit(1)

    resize_gif_by_width(input_file, output_file, width)
