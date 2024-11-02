import csv
import os

def annot(dir_name:str,a_file: str) -> None:
    """
    Создает аннотацию, csv файл, заносятся относительный и абсолютный пути.
    :param dir_name: Директория с изображениями
    :param a_file:csv файл для аннотации
    :return: None
    """
    with open(a_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Relative path', 'Absolute path'])
        for filename in os.listdir(dir_name):
            real=os.path.relpath(os.path.join(dir_name,filename),start=dir_name)
            absolut=os.path.abspath(os.path.join(dir_name,filename))
            writer.writerow([real,absolut])