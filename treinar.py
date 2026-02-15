from ultralytics import YOLO
import os

# 1. Carrega o modelo YOLOv8 Nano (leve e rápido para o seu PC)
model = YOLO("yolov8n.pt")

# 2. Inicia o treinamento
# O 'data' aponta para o arquivo que o Roboflow baixou
results = model.train(
    data="data.yaml", 
    epochs=50,      # 50 épocas é um bom número para um artigo acadêmico
    imgsz=640,      # Tamanho padrão de imagem
    plots=True      # ESSENCIAL: gera os gráficos para o seu relatório
)