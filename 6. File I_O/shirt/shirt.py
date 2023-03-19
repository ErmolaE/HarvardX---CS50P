import sys
from os.path import splitext
from PIL import Image, ImageOps


def main():
    old, new = check_com_line_arg()
    create_photo(old, new)

def check_com_line_arg():
    try:
        assert len(sys.argv) > 2, "Too few command-line arguments"
        assert len(sys.argv) < 4, "Too many command-line arguments"
        assert sys.argv[1].endswith((".jpg", ".png", ".jpeg")) == True, "Invalid input"
        assert sys.argv[2].endswith((".jpg", ".png", ".jpeg")) == True, "Invalid output"
        old_extensions = splitext(sys.argv[1])
        new_extensions = splitext(sys.argv[2])
        assert old_extensions[1] == new_extensions[1], "Input and output have different extensions"
        return sys.argv[1], sys.argv[2]
    except AssertionError as message:
        sys.exit(message)

def create_photo(old, new):
    try:
        shirt = Image.open("shirt.png")
        size = shirt.size
        input_image = Image.open(old)
        muppet = ImageOps.fit(input_image, size)
        muppet.paste(shirt, shirt)
        muppet.save(new)
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()