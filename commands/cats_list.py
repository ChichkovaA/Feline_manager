import os
from commands._get_cat_folder_path import get_cat_folder_path


def cats_list():
    base_dir, cats_dir, cat_name_dir = get_cat_folder_path('')

    if not os.path.exists(cats_dir):
        os.makedirs(cats_dir)
        print(f"Папка 'cats' была создана в {base_dir}")

    cat_folders = os.listdir(cats_dir)
    if len(cat_folders) == 0:
        print("Еще нет ни одной папки кота")
        return
    print(*cat_folders, sep="\n")
    return cat_folders
