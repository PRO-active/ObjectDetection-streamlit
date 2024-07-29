import streamlit as st
import torch
from PIL import Image
import numpy as np

# モデルをロードする関数
def load_model():
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=False)
    model.load_state_dict(torch.load('/app/yolov5s_state_dict.pt', map_location=torch.device('cpu')))
    return model

# 保存済みモデルのロード
model = load_model()

# タイトルと説明
st.title('YOLOv5 Object Detection App')
st.write('Upload an image and the YOLOv5 model will detect objects in the image.')

# 画像アップロード
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Detecting...")

    # 画像をYOLOv5モデルに渡す
    results = model(image)

    # 結果を表示
    results.render()
    st.image(np.squeeze(results.imgs), caption='Detected Image.', use_column_width=True)