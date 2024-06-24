FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get install -y libgl1-mesa-glx git

RUN git clone https://github.com/ultralytics/yolov5.git

RUN pip install torch torchvision Pillow numpy streamlit

COPY app.py .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501"]
