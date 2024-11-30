import argparse


def value_input() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('path_image', type=str, help='Путь к изображению')
    parser.add_argument('path_new_image', type=str, help='Путь для сохранения')
    arg = parser.parse_args()
    return arg