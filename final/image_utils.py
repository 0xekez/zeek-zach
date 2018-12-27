import PIL
from PIL import Image
import os

def resize_image(infile, size):
    outfile = os.path.splitext(infile)[0] + "_small.png"
    im = Image.open(infile)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(outfile)
    return outfile
