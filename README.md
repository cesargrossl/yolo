# yolo
Deep Learning Yolo


50 epochs completed in 1.933 hours.
Optimizer stripped from C:\Users\Toco\Desktop\deeplearning\yolo\runs\detect\train2\weights\last.pt, 6.2MB
Optimizer stripped from C:\Users\Toco\Desktop\deeplearning\yolo\runs\detect\train2\weights\best.pt, 6.2MB

Validating C:\Users\Toco\Desktop\deeplearning\yolo\runs\detect\train2\weights\best.pt...
Ultralytics 8.4.14  Python-3.12.3 torch-2.9.1+cpu CPU (Intel Core i5-9400F 2.90GHz)
Model summary (fused): 73 layers, 3,005,843 parameters, 0 gradients, 8.1 GFLOPs



0: 480x640 1 pallet, 51.4ms


Outros números que podem aparecer no seu terminal:
Se você está olhando para as linhas que aparecem no console, como:
0: 480x640 1 pallet, 51.4ms

480x640: É a resolução da imagem que a RealSense está enviando (largura x altura).

1 pallet: É a quantidade de paletes que ele encontrou naquele frame específico.

51.4ms (Milissegundos): É a Velocidade (Inference Speed). É o tempo que o seu computador levou para "pensar" e identificar o palete naquela foto.

Dica: Como 1 segundo tem 1000ms, se ele faz em 50ms, ele consegue processar cerca de 20 imagens por segundo (20 FPS), o que é ótimo para tempo real!
# Detecção de Paletes em Tempo Real com YOLOv8 e Intel RealSense D415

Este projeto consiste em um sistema de visão computacional capaz de identificar paletes em tempo real utilizando o modelo de deep learning **YOLOv8** e a câmera de profundidade **Intel RealSense D415**.

## 🚀 Funcionalidades
* Detecção automatizada de paletes em ambientes logísticos.
* Processamento de vídeo em tempo real (média de 20 FPS).
* Integração direta com o SDK da Intel RealSense (extração de frames RGB).
* Alta precisão com índices de confiança superiores a 85%.

## 🛠️ Tecnologias Utilizadas
* **Python 3.12+**
* **YOLOv8 (Ultralytics)**: Arquitetura de detecção de objetos.
* **Roboflow**: Gestão, anotação e exportação do dataset.
* **Intel RealSense SDK (pyrealsense2)**: Captura de dados da câmera D415.
* **OpenCV**: Processamento de imagem e interface visual.

## 📦 Estrutura do Projeto
```text
├── datasets/           # Imagens e labels de treino (YOLOv8 format)
├── runs/               # Resultados e pesos do treinamento
│   └── detect/
│       └── train/
│           └── weights/
│               └── best.pt  # Melhor modelo treinado
├── treinar.py          # Script de treinamento do modelo
├── teste_camera.py     # Script de inferência em tempo real com RealSense
└── README.md