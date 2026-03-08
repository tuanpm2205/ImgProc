from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model("baothanhnien_input.jpg")

results[0].save()
