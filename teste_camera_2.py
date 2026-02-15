import pyrealsense2 as rs
import numpy as np
import cv2
from ultralytics import YOLO

# 1. Carrega o modelo que você treinou
# Certifique-se de que o caminho para o 'best.pt' está correto
model = YOLO('runs/detect/train2/weights/best.pt')

# 2. Configura a câmera Intel RealSense
pipeline = rs.pipeline()
config = rs.config()

# Configura o fluxo de cor (RGB)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Inicia a câmera
pipeline.start(config)

print("Câmera RealSense iniciada. Pressione 'q' para sair.")

try:
    while True:
        # Aguarda um novo conjunto de frames
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        if not color_frame:
            continue

        # Converte a imagem da RealSense para o formato que o OpenCV entende (numpy array)
        img = np.asanyarray(color_frame.get_data())

        # 3. Faz a detecção do Pallet
        # conf=0.5 significa que ele só mostra se tiver mais de 50% de certeza
        results = model(img, conf=0.5)

        # 4. Desenha os resultados na tela
        annotated_frame = results[0].plot()

        # Mostra a imagem na janela
        #cv2.imshow('Detecção de Pallets - RealSense', annotated_frame)
        cv2.imshow('Detectando Pallets', annotated_frame)

        # Sai se apertar a tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Para a câmera e fecha as janelas
    pipeline.stop()
    cv2.destroyAllWindows()