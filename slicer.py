import os
import image_slicer
import random
import math
import copy
from PIL import Image, ImageDraw

def draw_rectangle(drawcontext, xy, outline=None,  width=5):
    (x1, y1), (x2, y2) = xy
    points = (x1, y1), (x2, y1), (x2, y2), (x1, y2), (x1, y1)
    drawcontext.line(points, fill=outline, width=width)

def slice(img_name, input_dir="input_images", output_dir="output_images", number_tiles=4, outline_width=2):
    tiles = image_slicer.slice(os.path.join(input_dir,img_name), number_tiles=number_tiles, save=False)
    rand_tiles = copy.deepcopy(tiles)
    image_ids = list(range(len(tiles)))
    random.shuffle(image_ids)
    for i in range(len(tiles)):
        rand_tiles[i].image = tiles[image_ids[i]].image
        draw_context = ImageDraw.Draw(rand_tiles[i].image)
        draw_rectangle(draw_context, [(0,0), (rand_tiles[i].image.width,rand_tiles[i].image.height)], outline='black', width=outline_width)
    image = image_slicer.join(rand_tiles)
    image.save(os.path.join(output_dir, img_name))


if __name__ == '__main__':
    input_dir = "input_images"
    output_dir = "output_images"
    number_tiles = 4
    outline_width = 2

    input_files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
    for img_file in input_files:
        slice(img_file, input_dir=input_dir, output_dir=output_dir, number_tiles=number_tiles, outline_width=outline_width)