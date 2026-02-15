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
