from ultralytics import YOLO

# Load a model
model = YOLO("YOLOv8x.yaml")  # build a new model from scratch

# Use the model
results = model.train(data="config.yaml", epochs=10) 