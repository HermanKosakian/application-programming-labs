import csv

class IIterator:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, mode='r', newline='', encoding='utf-8')
        self.reader = csv.reader(self.file)
        self.current_row = None


    def __iter__(self) -> 'IIterator':
        return self

    def __next__(self):
        try:
            self.current_row = next(self.reader)
            file_path = self.current_row[0]
            return file_path
        except StopIteration:
            self.file.close()
            raise
        except IndexError:
            raise StopIteration
