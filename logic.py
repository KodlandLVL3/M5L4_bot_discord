import cv2


def process_image(image_path, output_path):
    # Загрузка предобученного классификатора для детектирования лиц
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Загрузка изображения
    image = cv2.imread(image_path)

    if image is None:
        print("Ошибка: Не удалось загрузить изображение.")
        return

    # Преобразование изображения в оттенки серого для улучшения производительности детектора
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Обнаружение лиц в изображении
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Размытие области вокруг каждого обнаруженного лица
    for (x, y, w, h) in faces:
        # Извлечение области лица
        face_region = image[y:y+h, x:x+w]

        # Применение размытия
        blurred_face = cv2.GaussianBlur(face_region, (99, 99), 30)

        # Замена области лица размытым изображением
        image[y:y+h, x:x+w] = blurred_face

    # Сохранение обработанного изображения
    cv2.imwrite(output_path, image)
    print(f"Изображение сохранено в {output_path}")


# Проверяем работу кода
process_image("face.png", "output.png")