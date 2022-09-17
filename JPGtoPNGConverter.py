import sys
import os
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/ exists, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# loop though Pokedex,
# convert images to png
# save them to the new folder