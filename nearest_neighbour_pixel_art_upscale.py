from PIL import Image
import numpy as np
from pathlib import Path

multiplier_number = 128
src_folder = Path("")

dest_folder = Path("")
dest_folder.mkdir(parents=True, exist_ok=True)


for image_file_path in src_folder.iterdir():
    image = Image.open(image_file_path)
    image = image.convert("RGB")

    img_arr = np.array(image)
    upscaled_img_arr = np.repeat(
        np.repeat(img_arr, multiplier_number, axis=0), multiplier_number, axis=1
    )

    Image.fromarray(upscaled_img_arr).save(
        dest_folder / f"{image_file_path.stem}_{image.width * multiplier_number}.png"
    )


# multiplier_number = 128

# for image_file_path in Path('/home/raven/Personal-Projects/Minecraft_ores/Ore_16x16_textures/').iterdir():


#     image = Image.open(image_file_path)
#     image = image.convert("RGB")

#     # Image object -> np.array returns a:
#     # Example a H = 3 and W = 2
#     #
#     # arr [ [[R,G,B], [R,G,B]], [[R,G,B], [R,G,B]], [[R,G,B], [R,G,B]] ]
#     # (Height, Width, Color Channels)

#     image_arr = np.array(image)

#     # x_coord = 0
#     # y_coord = 0

#     # pixel = image_arr[x_coord, y_coord]

#     # .shape return a tuple of length of an array
#     # [:2] hence get the lengths of [0]-height and [1]-width (till 2)
#     old_h, old_w = image_arr.shape[:2]

#     new_h, new_w = old_h * multiplier_number , old_w * multiplier_number

#     upscaled_image = np.empty((new_h, new_w, 3), dtype = np.uint8)

#     new_y_coord = 0
#     new_x_coord = 0

#     for y_coord in range(0, old_h):
#         for x_coord in range(0, old_w):
#             print(y_coord, x_coord)
#             print("___")

#             for dx in range(multiplier_number):
#                 new_x_coord = x_coord*multiplier_number + dx
#                 for dy in range(multiplier_number):
#                     new_y_coord = y_coord*multiplier_number + dy

#                     upscaled_image[new_y_coord, new_x_coord] = image_arr[y_coord, x_coord]
#                     print(new_y_coord, new_x_coord)


#     new_image = Image.fromarray(upscaled_image)

#     new_folder_path = '/home/raven/Personal-Projects/Minecraft_ores/Ore_2k_textures/'
#     Path(new_folder_path).mkdir(parents=True, exist_ok=True)

#     original_filename = image_file_path.stem

#     new_filename = f"{original_filename}_2k.png"

#     new_image_path = Path(new_folder_path) / new_filename

#     new_image.save(new_image_path)
