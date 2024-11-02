import argparse

def inp() -> argparse.Namespace:
    """
    Функция, позволяющая осуществить ввод ключевого слова, пути к директории, пути к файлу для аннотации
    :return: аргументы
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('keyword', type=str, help='Ключевое слово')
    parser.add_argument('dir', type=str, help='Путь к директории')
    parser.add_argument('a_file', type=str, help='Путь к файлу для аннотации')
    arg = parser.parse_args()
    return arg