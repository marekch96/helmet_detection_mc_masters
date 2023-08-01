from ultralytics import YOLO

# Load a model
model = YOLO('yolov8l.yaml')  # build a new model from scratch

# Use the model
results = model.train(data="config.yaml", epochs=100)