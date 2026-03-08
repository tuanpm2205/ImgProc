from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model("cats.jpg")

results[0].save()
