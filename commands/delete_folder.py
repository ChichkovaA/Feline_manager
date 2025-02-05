import os
import shutil
from commands._get_cat_folder_path import get_cat_folder_path


def delete_folder(cat_name):
    base_dir, cats_dir, cat_name_dir = get_cat_folder_path(cat_name)

    if not os.path.exists(cats_dir):
        print("Еще нет ни одной папки кота")
        return
    if not os.path.exists(cat_name_dir):
        print("Нет папки кота с таким именем")
        return
    try:
        shutil.rmtree(cat_name_dir)
        print(f"Папка кота {cat_name} удалена")
    except Exception as e:
        print(f"Папка не была удалена. Ошибка: {e}")
