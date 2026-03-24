from ultralytics import YOLO
import os
import shutil

# Load pretrained model
model = YOLO("yolov8n.pt")   # you can use yolov8s.pt for better accuracy

input_folder = "patches"
output_folder = "filtered_images"

os.makedirs(output_folder, exist_ok=True)

# COCO class id for car = 2
CAR_CLASS_ID = 2

for img_name in os.listdir(input_folder):
    img_path = os.path.join(input_folder, img_name)

    results = model(img_path, conf=0.25)

    keep = False

    for r in results:
        if r.boxes is not None:
            for cls in r.boxes.cls:
                if int(cls) == CAR_CLASS_ID:
                    keep = True
                    break

    if keep:
        shutil.copy(img_path, os.path.join(output_folder, img_name))