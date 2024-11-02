import os

from icrawler.builtin import GoogleImageCrawler

def d_image(dir_name: str,keyword: str) -> None:
    """
    Функция выполняет установку изображения с помощью GoogleImageCrawler, перед этим создает директорий(если необходимо)
    :param dir_name: директория, в которую мы сохраняем изображения
    :param keyword: ключевое слово
    :return: None
    """
    if not(os.path.exists(dir_name)):
        os.mkdir(dir_name)
    google_crawler = GoogleImageCrawler(
        storage={'root_dir': dir_name})
    google_crawler.crawl(keyword=keyword, max_num=50)
