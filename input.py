import argparse


def value_input() -> argparse.Namespace:
    """
    Функция, позволяющая осуществить ввод пути к директории, пути к файлу для аннотации, максимальную ширину и высоту
    :return: аргументы
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir_name', type=str, help='Путь к директории')
    parser.add_argument('-f', '--annotation_file', type=str, help='Путь к файлу для аннотации')
    parser.add_argument('-wm', '--width', type=int, help='Максимальная ширина')
    parser.add_argument('-hm', '--height', type=int, help='Максимальная высота')
    args = parser.parse_args()
    return args