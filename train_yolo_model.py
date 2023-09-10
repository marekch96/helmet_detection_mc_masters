from ultralytics import YOLO
import cv2


# Load a model
model = YOLO('yolov8l.yaml')  # build a new model from scratch most powerful yolo 


# Use the model
results = model.train(data='config.yaml',epochs=50,batch=8,name='big_yolov8x') #batch size incresed from 8 to 16  + 50 epochs #max vram that rtx 4070 can handle 


#yolo task=detect mode=predict model=helmet_motorcycle_detection_best.pt source='input/video_3.mp4' show=True

