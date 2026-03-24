import os
import cv2
from patchify import patchify
import numpy as np

# Input & Output folders
input_folder = "archive/DOTA/val/images"
output_folder = "patches"

os.makedirs(output_folder, exist_ok=True)

patch_size = 640

for img_name in os.listdir(input_folder):
    img_path = os.path.join(input_folder, img_name)

    # Read image
    image = cv2.imread(img_path)

    if image is None:
        continue

    h, w, c = image.shape

    if h < 640 or w < 640:
        continue

    # Make dimensions divisible by 640
    new_h = (h // patch_size) * patch_size
    new_w = (w // patch_size) * patch_size

    image = image[:new_h, :new_w]

    # Apply patchify
    patches = patchify(image, (patch_size, patch_size, 3), step=patch_size)

    patch_id = 0

    for i in range(patches.shape[0]):
        for j in range(patches.shape[1]):

            patch = patches[i, j, 0]

            patch_filename = f"{os.path.splitext(img_name)[0]}_patch_{patch_id}.png"
            patch_path = os.path.join(output_folder, patch_filename)

            cv2.imwrite(patch_path, patch)
            patch_id += 1

print("Done creating patches ✅")


# img = (Image.open("archive/DOTA/test/images/P0006.png"))
# img_arr=np.asarray(img)

# patches=patchify(img_arr,(640,640,3),step=640)

# os.makedirs("patches",exist_ok=True)

# count=0
# for i in range(patches.shape[0]):
#     for j in range(patches.shape[1]):
#         patch = patches[i, j, 0]   # remove that extra dimension
        
#         patch_img = Image.fromarray(patch)
#         patch_img.save(f"patches/patch_{count}.jpg")
        
#         count += 1

# print("Done")

# patch_img=Image.fromarray(patches)