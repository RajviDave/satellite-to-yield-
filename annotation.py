from ultralytics import YOLO
import os

# Load pretrained model
model = YOLO("yolov8s.pt")   # use 'yolov8s.pt' for better accuracy

input_folder = "filtered_images"
label_folder = "labels"

os.makedirs(label_folder, exist_ok=True)

CAR_CLASS_ID = 2  # COCO class for car

for img_name in os.listdir(input_folder):
    img_path = os.path.join(input_folder, img_name)

    # Run detection (LOW CONF for small objects)
    results = model(img_path, conf=0.15)

    label_path = os.path.join(label_folder, img_name.replace(".png", ".txt"))

    with open(label_path, "w") as f:
        for r in results:
            if r.boxes is not None:
                boxes = r.boxes.xywhn  # normalized (YOLO format)
                classes = r.boxes.cls

                for box, cls in zip(boxes, classes):
                    if int(cls) == CAR_CLASS_ID:
                        x, y, w, h = box.tolist()
                        f.write(f"0 {x} {y} {w} {h}\n")  # class 0 = car