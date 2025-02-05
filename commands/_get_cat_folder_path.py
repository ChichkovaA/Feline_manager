import os


def get_cat_folder_path(cat_name):
    """Унифицирует запись имеми и возвращает пути к основной папке,
    папке cats и папке конкретного кота."""
    cat_name = cat_name.strip().lower().capitalize()
    base_dir = os.path.abspath(os.getcwd())
    cats_dir = os.path.join(base_dir, "cats")
    cat_name_dir = os.path.join(cats_dir, cat_name)

    return base_dir, cats_dir, cat_name_dir
