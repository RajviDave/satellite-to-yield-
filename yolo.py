# #understadn all the type of dataset
# #train model
# #Do Gee
# from ultralytics import YOLO

# # Load a model
# model = YOLO("yolo26n.pt")

# # # Train the model
import kagglehub
import torch

# Download latest version
# path = kagglehub.dataset_download("hassanmojab/xview-dataset")

weights=torch.load('yolo26n.pt',weights_only=False)
print(weights.keys())