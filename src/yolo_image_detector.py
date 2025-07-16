from ultralytics import YOLO
import os
import json
from pathlib import Path
from PIL import Image

# Load pre-trained model (YOLOv8n for speed, YOLOv8m/l/x for accuracy)
model = YOLO("yolov8n.pt")  # Can change to yolov8m.pt etc.

# Directory containing media scraped in Task 1
image_dir = Path("data/raw/images")
results_output = []

# Iterate through images
for image_file in image_dir.glob("*.jpg"):
    result = model(image_file)[0]  # single prediction
    for box in result.boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        label = result.names[class_id]
        
        # Store detection result
        results_output.append({
            "image_name": image_file.name,
            "detected_class": label,
            "confidence": round(confidence, 3)
        })

# Save detections for loading
with open("data/raw/yolo_detections.json", "w") as f:
    json.dump(results_output, f, indent=2)
