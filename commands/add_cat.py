import os
from commands._get_cat_folder_path import get_cat_folder_path


def add_cat(cat_name: str):
    base_dir, cats_dir, cat_name_dir = get_cat_folder_path(cat_name)

    if not os.path.exists(cats_dir):
        os.makedirs(cats_dir)
        print(f"Папка 'cats' была создана в {base_dir}")

    if os.path.exists(cat_name_dir):
        print(f"Папка {cat_name} уже существует в {cats_dir}")
    else:
        os.makedirs(cat_name_dir)
        print(f"Папка {cat_name} была создана в {cats_dir}")
