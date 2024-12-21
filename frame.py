import cv2
import matplotlib.pyplot as plt
import pandas as pd


def create_df(annotation_file: str) -> pd.DataFrame:
    """
    Функция создает DataFrame из CSV файла с аннотацией.
    :param annotation_file: CSV файл с аннотацией
    :return: DataFrame с абсолютными и относительными путями
    """
    df = pd.read_csv(annotation_file)
    df.columns = ['Relative_path','Absolute_path']
    return df


def dimensions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Функция добавляет информацию о высоте, ширине и глубине изображений в DataFrame.
    :param df: DataFrame с аннотацией изображений
    :return: DataFrame с добавленными колонками для высоты, ширины и глубины
    """
    height, width, channels = [], [], []
    for abs_path in df['Absolute_path']:
            img = cv2.imread(abs_path)
            if img is not None:
                height.append(img.shape[0])
                width.append(img.shape[1])
                channels.append(img.shape[2])
            else:
                raise FileNotFoundError(f"File {abs_path} not found.")
    df['Height'] = height
    df['Width'] = width
    df['Channels'] = channels
    return df


def im_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Вычисляет статистическую информацию для столбцов с размерами изображений.
    :param df: DataFrame с аннотацией изображений, содержащий колонки 'Ширина', 'Высота', 'Глубина'
    :return: DataFrame со статистической информацией
    """
    stats = df[["Height", "Width", "Channels"]].describe()
    return stats


def filter_size(df: pd.DataFrame, width: int, height: int) -> pd.DataFrame:
    """
    Фильтрует DataFrame по максимальным значениям ширины и высоты изображений.
    :param df: DataFrame с аннотацией изображений, содержащий колонки 'Ширина' и 'Высота'
    :param width: Значение максимальной ширины, заданное пользователем через терминал
    :param height: Значение максимальной высоты, заданное пользователем через терминал
    :return: Отфильтрованный DataFrame
    """
    filtered_df = df[(df['Width'] <= width) & (df['Height'] <= height)]
    return filtered_df


def area(df: pd.DataFrame) -> pd.DataFrame:
    """
    Добавляет новый столбец с площадью изображения в DataFrame.
    :param df: DataFrame с аннотацией изображений, содержащий колонки 'Ширина' и 'Высота'
    :return: DataFrame с добавленным столбцом 'Площадь'
    """
    df['Area'] = df['Width'] * df['Height']
    return df


def sort_area(df: pd.DataFrame) -> pd.DataFrame:
    """
    Сортирует DataFrame по площади изображений от меньшего к большему.
    :param df: DataFrame с колонкой 'Площадь'
    :return: Отсортированный DataFrame
    """
    sorted_df = df.sort_values(by='Area')
    return sorted_df


def hist_area(df: pd.DataFrame):
    """
    Строит гистограмму распределения площадей изображений.
    :param df: DataFrame с колонкой 'Площадь'
    """
    plt.figure(figsize=(10, 5))
    plt.hist(df['Area'], bins=25, color='red', edgecolor='black')
    plt.title('Distribution of image areas')
    plt.xlabel('Area')
    plt.ylabel('Number of images')
    plt.show()