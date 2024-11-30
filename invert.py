import cv2
import matplotlib.pyplot as plt
import numpy as np


def proportions(path_image:str) -> None:
    """
    Функция вывода высоты и ширины изображения
    :param path_image: путь к изображению
    :return: None
    """
    img = cv2.imread(path_image)
    height, width, channels=img.shape
    print(f"Высота изображения: {height}, Ширина изображения: {width}")


def invert_image(image: np)->np:
    """
    Функция преобразования изображения в инвертированное
    :param image:массив с цветными пикселями(изображение)
    :return:новый массив с пикселями инвертированного цвета
    """
    return cv2.bitwise_not(image)


def save_invert(in_img: np,path_invert: str)->None:
    """
    Функция сохранения нового изображения
    :param in_img: инвертированное изображение
    :param path_invert:путь для создания нового изображения
    :return: None
    """
    cv2.imwrite(path_invert, in_img)


def image_output(image: np,invert: np)->None:
    """
    Функция вывода исходного изображения и измененного
    :param image: массив с цветными пикселями(изображение)
    :param invert: массив с инвертированными пикселями(инвертированное изображение)
    :return: None
    """
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    in_img=cv2.cvtColor(invert, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title('Исходное изображение')
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.imshow(in_img)
    plt.title('Обработанное изображение')
    plt.axis('off')
    plt.tight_layout()
    plt.show()