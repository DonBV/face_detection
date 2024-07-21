import cv2
import os
from mtcnn import MTCNN

# Инициализация детектора MTCNN
detector = MTCNN()

# Убедитесь, что путь к видеофайлу правильный
video_path = os.path.expanduser("~/Desktop/Your_video_name.mp4")

# Захват видео
cap = cv2.VideoCapture(video_path)

# Проверьте, удалось ли открыть видеофайл
if not cap.isOpened():
    print("Ошибка: не удалось открыть видеофайл")
    exit()

# Получаем ширину, высоту и FPS исходного видео
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Определяем кодек и создаем объект VideoWriter
output_path = os.path.expanduser("~/Desktop/Your_video_name_output_mtcnn.mp4")
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Кодек для формата MP4
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

while True:
    # Считываем кадр
    ret, frame = cap.read()
    
    # Проверяем, удалось ли считать кадр
    if not ret:
        break
    
    # Обнаруживаем лица
    results = detector.detect_faces(frame)
    
    # Рисуем прямоугольники вокруг лиц
    for result in results:
        x, y, width, height = result['box']
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 2)
    
    # Записываем кадр в выходной видеофайл
    out.write(frame)

# Освобождаем захват видео и закрываем объект VideoWriter
cap.release()
out.release()
