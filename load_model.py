import torch

# YOLOv5のモデルをロード
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# モデルを保存
torch.save(model, 'yolov5s.pt')