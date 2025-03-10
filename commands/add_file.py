import os
import shutil
from commands._get_cat_folder_path import get_cat_folder_path


def add_file(file_path, cat_name):
    if not os.path.exists(file_path):
        print(f"Ошибка: файл или папка {file_path} не найден(а)")
        return

    base_dir, cats_dir, cat_name_dir = get_cat_folder_path(cat_name)
    file_name = os.path.basename(file_path)
    file_dst = os.path.join(cat_name_dir, file_name)

    try:
        # Создаем структуру каталога, если ее нет
        if not os.path.exists(cats_dir):
            os.makedirs(cats_dir)
            print(f"Папка 'cats' была создана в {base_dir}")
        if not os.path.exists(cat_name_dir):
            os.makedirs(cat_name_dir)
            print(f"Папка {cat_name} была создана в {cats_dir}")
        # Копируем, если это файл
        if os.path.isfile(file_path):
            if os.path.exists(file_dst):
                print(f"Файл {file_name} уже существует в папке {cat_name}, копирование отменено.")
                return
            shutil.copy2(file_path, file_dst)
            print(f"Файл {file_name} добавлен в папку {cat_name}")
            return
        # Копируем, если это папка
        if os.path.isdir(file_path):
            if os.path.isfile(file_path):
                print(f"Папка {file_name} уже существует в папке {cat_name}, копирование отменено.")
                return
            shutil.copytree(file_path, file_dst)
            print(f"Папка {file_name} добавлена в папку {cat_name}")
            return
        print(f"Ошибка: '{file_path}' не является ни файлом, ни папкой. Копирование отменено")
    except Exception as e:
        print(f"Произошла ошибка при копировании: {e}")
