from anot import annotation_creation
from input import value_input
from frame import *


def main():
    try:
        args=value_input()
        annotation_creation(args.dir_name,args.annotation_file)
        df=create_df(args.annotation_file)
        print("DataFrame создан:")
        print(df)
        dimensions(df)
        print("Размеры изображений :")
        print(df)
        print("Статистика изображений:")
        print(im_statistics(df))
        df=filter_size(df,args.width,args.height)
        print("Изображения после фильтрации по размеру:")
        print(df)
        df=area(df)
        print("Колонка с площадью:")
        print(df)
        df=sort_area(df)
        print("DataFrame отсортирован по площади:")
        print(df)
        hist_area(df)
    except Exception as e:(
        print(f'Error: {e}'))


if __name__ == '__main__':
    main()