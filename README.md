# Image  Puzzle

A simple python program that slices a picture into N tiles, shuffle the tiles and recreate an image.

## Description

The program reads all images contained in the "Input directory" and does the following for every image:
* Slices the image into N tiles
* Shuffles the tiles
* Adds a small border of M pixels to every tile (it actually paints a line over the existing pixels of the tile)
* Recreates an image with the shuffled and update tiles

Options:
* number_tiles = the number of tiles the input image will be split into
* outline_width = the width of the border painted around every tile

## Note

I only tested it with ".png" images

## Potential improvements
* Handle additional image formats
* Ensure original adjacent tiles are not adjacent in the final image
* Define how to tile images  (#row, #columns)$
* ...

### Dependencies

* Python 3.7 (should probably work with prior versions)
* image_slicer 


### Installing

Nothing special

### Executing program

Just run it 

## Help

No help required ...

## Authors

Simon Ruffieux


## License

Feel free to reuse this project as you wish

## Acknowledgments

* Thanks to image_slicer developers
