import numpy as np
from sys import argv
from os import path
from PIL import Image

if __name__ == "__main__":
    if len(argv) != 3:
        print("Error, usage python3 createImage.py <file> <output>")
        exit(1)

    if not path.exists(argv[1]):
        print("Error, file does not exist")
        exit(1)

    file = np.loadtxt(argv[1], dtype="i", delimiter=",")
    img = Image.fromarray(np.uint8(file * 255), "L")
    img.save("{}".format(argv[2]))