import os

from ultralytics import YOLO

model_path = os.path.join('ML', 'runs', 'detect', 'train2', 'weights', 'best.pt')
model = YOLO(model_path)
model.export(format="tflite", imgsz=640)  # Adjust imgsz if needed