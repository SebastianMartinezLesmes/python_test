import cv2
from fer import FER

# Inicializa detector de emociones
detector = FER(mtcnn=True)

# Abre la cámara (0 = cámara predeterminada)
cam = cv2.VideoCapture(0)

print("Presiona 'q' para salir")

while True:
    ret, frame = cam.read()
    if not ret:
        break

    # Detecta emociones en el frame actual
    result = detector.detect_emotions(frame)

    for face in result:
        (x, y, w, h) = face["box"]
        emotion, score = max(face["emotions"].items(), key=lambda item: item[1])
        
        # Dibuja rectángulo y texto con emoción
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f'{emotion} ({score:.2f})', (x, y - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    cv2.imshow("Detector de emociones", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
