import os
import shutil
import random

# paths
source_folder = "robo_flow"
output_folder = "dataset"

# create folders
splits = ["train", "valid", "test"]
for split in splits:
    os.makedirs(os.path.join(output_folder, split, "images"), exist_ok=True)
    os.makedirs(os.path.join(output_folder, split, "labels"), exist_ok=True)

# get all images
images = [f for f in os.listdir(source_folder) if f.endswith((".png", ".jpg", ".jpeg"))]

# shuffle
random.shuffle(images)

# split ratios
train_split = int(0.7 * len(images))
val_split = int(0.2 * len(images))

train_images = images[:train_split]
val_images = images[train_split:train_split + val_split]
test_images = images[train_split + val_split:]

def move_files(image_list, split):
    for img in image_list:
        base = os.path.splitext(img)[0]
        label = base + ".txt"

        # paths
        src_img = os.path.join(source_folder, img)
        src_lbl = os.path.join(source_folder, label)

        dst_img = os.path.join(output_folder, split, "images", img)
        dst_lbl = os.path.join(output_folder, split, "labels", label)

        # move
        shutil.copy(src_img, dst_img)
        if os.path.exists(src_lbl):
            shutil.copy(src_lbl, dst_lbl)

# move data
move_files(train_images, "train")
move_files(val_images, "valid")
move_files(test_images, "test")

print("✅ Dataset split complete!")