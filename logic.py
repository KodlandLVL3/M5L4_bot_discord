import cv2


def process_image(image_path, output_path):
    # Загрузка предобученного классификатора для детектирования лиц
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Загрузка изображения
    image = 

    # Преобразование изображения в оттенки серого для улучшения производительности детектора
    gray = 

    # Обнаружение лиц в изображении
    faces = 

    # Размытие области вокруг каждого обнаруженного лица
    for (x, y, w, h) in faces:
        # Извлечение области лица
        face_region = image[y:y+h, x:x+w]

        # Применение размытия
        blurred_face = 

        # Замена области лица размытым изображением
        image[y:y+h, x:x+w] = blurred_face

    # Сохранение обработанного изображения
    


# Проверяем работу кода
process_image("face.png", "output.png")