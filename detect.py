from ultralytics import YOLO

model = YOLO("yolov8x.pt")

results = model("cats.jpg")

results[0].save()
