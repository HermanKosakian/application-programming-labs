import cv2
import matplotlib.pyplot as plt
import numpy as np


def histogram_creation(img: np)-> tuple:
    """
    Функция создает гистограмму цветного изображения
    :param img:массив из пикселей(цветное изображение в формате rgb)
    :return:гистограмма для каждого канала, содержащая количество пикселей для каждого из 256 уровней цвета
    """
    image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    r, g, b = cv2.split(image_rgb)
    hist_r, bins_r = np.histogram(r.flatten(), bins=256, range=[0, 256])
    hist_g, bins_g = np.histogram(g.flatten(), bins=256, range=[0, 256])
    hist_b, bins_b = np.histogram(b.flatten(), bins=256, range=[0, 256])
    return hist_r,hist_g,hist_b

def histogram_drawing(hist_r: np, hist_g: np, hist_b: np) -> None:
    """
    Функция рисует гистограмму на основе переданного массива
    :param hist_r: данные для гистограммы красного канала
    :param hist_g: данные для гистограммы зеленого канала
    :param hist_b: данные для гистограммы синего канала
    :return: None
    """
    plt.figure(figsize=(10, 5))
    plt.title('Color Histogram')
    plt.xlabel('Pixel Values')
    plt.ylabel('Frequency')
    plt.plot(hist_r, color='red', label='Red Channel')
    plt.plot(hist_g, color='green', label='Green Channel')
    plt.plot(hist_b, color='blue', label='Blue Channel')
    plt.legend()
    plt.xlim([0, 255])
    plt.show()