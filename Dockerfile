FROM python:3.8

WORKDIR /app

RUN apt-get update && apt-get install -y libgl1-mesa-glx git

RUN git clone https://github.com/ultralytics/yolov5.git

RUN pip install -r yolov5/requirements.txt

RUN pip install torch torchvision Pillow numpy streamlit opencv-python

COPY load_model.py .
RUN python load_model.py

COPY app.py .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501"]
