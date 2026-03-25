from ultralytics import YOLO

# 1. Load pretrained model
model = YOLO("yolov8s.pt")

model.train(
    data="data.yaml",   # path to your yaml file
    epochs=50,          # increase to 100 later
    imgsz=640,         # VERY IMPORTANT for small cars
    batch=1,            # adjust based on GPU
    name="car_detection_model",
    workers=0
)