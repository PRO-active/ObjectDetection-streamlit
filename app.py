import streamlit as st
import torch
from PIL import Image
import numpy as np

model = torch.load('/app/yolov5s.pt')

st.title('YOLOv5 Object Detection App')
st.write('Upload an image and the YOLOv5 model will detect objects in the image.')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Detecting...")

    results = model(image)

    results.render()
    st.image(np.squeeze(results.imgs), caption='Detected Image.', use_column_width=True)
