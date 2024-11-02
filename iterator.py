class IIterator:
    def __init__(self, path: str) -> None:
        """
        Заносит путь в список.
        :param path: Путь к файлу с аннотацией
        """
        self.images = []
        self.index = 0
        with open(path, 'r', encoding='utf-8') as file:
            next(file)
            for line in file:
                parts = line.strip().split(',')
                abs_path = parts[1]
                self.images.append(abs_path)


    def __iter__(self) -> 'IIterator':
        return self


    def __next__(self) -> str:
        """
        Эта функция получает следующий элемент из списка абсолютных путей к изображениям.
        :return: Путь к текущему изображению
        """
        if self.index < len(self.images):
            image_path = self.images[self.index]
            self.index += 1
            return image_path
        else:
            raise StopIteration