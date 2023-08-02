from ultralytics import YOLO
import cv2


# Load a model
model = YOLO('yolov8l.yaml')  # build a new model from scratch most powerful yolo 


# Use the model
results = model.train(data='config.yaml',epochs=50,batch=8,name='helmet_motorbike_custom_modelv8l_50e')