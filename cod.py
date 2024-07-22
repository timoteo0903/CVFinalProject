# import streamlit as st
import cv2
import numpy as np
from PIL import Image
from ultralytics import YOLO
from envido import contarEnvido
from canto import hablar

# Cargar el modelo YOLOv8
model_path = r"train1344/train13/weights/best.pt" 
model = YOLO(model_path)

def predict(image):
    # Realiza la predicción usando el modelo YOLOv8
    results = model.predict(image)
    return results

def draw_boxes(image, results):
    top3_labels = []
    for result in results:
        # Ordenar las detecciones por confianza en orden descendente
        sorted_boxes = sorted(result.boxes, key=lambda box: box.conf[0], reverse=True)
        
        # Tomar las 3 detecciones con mayor confianza
        top3_boxes = sorted_boxes[:3]
        
        # Recorrer las 3 detecciones principales
        for box in top3_boxes:
            x_min, y_min, x_max, y_max = map(int, box.xyxy[0])
            conf = box.conf[0]
            cls = int(box.cls[0])
            label = f'{model.names[cls]} {conf:.2f}'
            top3_labels.append(label.split()[0])  # Almacena solo el nombre de la clase
            cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
            cv2.putText(image, label, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return image, top3_labels
def main():
    # Abrir la webcam
    cap = cv2.VideoCapture(0)
    frames_thr = 5
    cont = 0
    while True:
        # Capturar frame-by-frame
        ret, frame = cap.read()

        if not ret:
            break
        # Realizar predicciones
        results = predict(frame)

        # Dibujar las bounding boxes
        frame, top3 = draw_boxes(frame, results)
        # Mostrar el frame con las detecciones

        if len(top3) == 3:
            cont += 1
            if cont >= frames_thr:
                txt = contarEnvido(top3)
                hablar(txt)

        cv2.imshow('YOLOv8 Object Detection', frame)
        # Salir con la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Liberar la cámara y cerrar todas las ventanas
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

