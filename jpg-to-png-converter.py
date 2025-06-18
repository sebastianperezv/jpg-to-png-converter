import sys
import os
from PIL import Image

# grab the fisrt and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

print(image_folder, output_folder)
# check if /new exists,if not create
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# loop through Pokedex,
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0] # returns a tuple
    # save to the new folder
    img.save(f'{output_folder}{clean_name}.png','png')# convert images to png
    print('All done')