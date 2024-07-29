import torch

# YOLOv5のモデルをロード
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# モデルのパラメータを保存
torch.save(model.state_dict(), 'yolov5s_state_dict.pt')