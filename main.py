import os
import time
import csv


def get_size(value):
    """
    расчитываем сколько занимает папка со всем содержимым внутри в мегабайтах.
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(value):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    size = float('{:.2f}'.format(total_size / (1024 * 1024)))
    return size


def folder_info(item):
    name = 'Папка'  # Первый столбик файла название элемента
    f_name = item.split('\\')[-1]
    folder_size = str(get_size(item)) + ' Mb'  # Расчитываем размер текущей патки.

    folder_time = time.strftime('%d.%m.%Y', time.localtime(os.stat(item).st_ctime)) # Время создания папки.
    fileCount = 0  # Счетчик, который будет считать сколько файлов находится внутри папки.

    # Цикл подсчета всех файлов в папке
    for d, dirs, files in os.walk(item):
        for f in files:
            fileCount += 1

    # print("{}: {}, размер: {}, Дата создания: {}".format(name, item, folder_size, folder_time))
    # Массив данных который будет записываться в csv файл
    data = {'name': name,
            'f_name': f_name,
            'f_size': folder_size,
            'f_time': folder_time,
            'count': fileCount}
    # Запись в csv
    with open("d:\\statistic.csv", 'a') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow((data['name'], data['f_name'], data['count'], data['f_size'], data['f_time']))


def file_info(item):
    name = 'Файл'
    f_name = item.split('\\')[-1]
    item_size = str('{:.2f}'.format(os.path.getsize(item) / 1024)) + ' kb'  # Размер файла в килобайтах.
    item_time = time.strftime('%d.%m.%Y', time.localtime(os.stat(item).st_mtime)) # Время изменения файла.
    count_file = ' '
    # print("{}: {}, размер: {}, Дата создания: {}".format(name, item, item_size, item_time))

    data = {'name': name,
            'f_name': f_name,
            'f_size': item_size,
            'f_time': item_time,
            'count': count_file}

    with open("d:\\statistic.csv", 'a') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow((data['name'], data['f_name'], data['count'], data['f_size'], data['f_time']))


def main(path):

    for folderpath, dirnames, filenames in os.walk(path):

        folder_info(folderpath)
        files = os.listdir(folderpath)
        files = [os.path.join(folderpath, file) for file in files]

        for file in files:
            if os.path.isfile(file):
                file_info(file)
            else:
                continue


if __name__ == '__main__':
    path = "d:\PyCharmProject\Example\! БС\\"
    main(path)