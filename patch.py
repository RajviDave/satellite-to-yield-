from patchify import patchify 
from PIL import Image
import os
import numpy as np

img = (Image.open("archive/DOTA/test/images/P0006.png"))
img_arr=np.asarray(img)

patches=patchify(img_arr,(640,640,3),step=640)

os.makedirs("patches",exist_ok=True)

count=0
for i in range(patches.shape[0]):
    for j in range(patches.shape[1]):
        patch = patches[i, j, 0]   # remove that extra dimension
        
        patch_img = Image.fromarray(patch)
        patch_img.save(f"patches/patch_{count}.jpg")
        
        count += 1

print("Done")

# patch_img=Image.fromarray(patches)
