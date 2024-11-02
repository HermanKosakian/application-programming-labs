from anot import annot
from input import inp
from crawler import d_image
from iterator import IIterator


def main() -> None:
    try:
        args = inp()
        d_image(args.dir, args.keyword)
        annot(args.dir, args.a_file)
        iterator = IIterator(args.a_file)
        for img in iterator:
            print(img)
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == '__main__':
    main()