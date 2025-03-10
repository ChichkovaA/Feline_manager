import os
import shutil


def delete_file(file_path):
    base_dir = os.path.abspath(os.getcwd())
    cats_dir = os.path.join(base_dir, "cats")
    file_path = os.path.abspath(file_path)

    if not os.path.exists(file_path):
        print(f"Ошибка: файл или папка {file_path} не найден(а)")
        return
    if os.path.commonpath([cats_dir, file_path]) != cats_dir:
        print(f"Ошибка: файл или папка {file_path} находядся вне папки 'cats'. Удаление запрещено")
        return
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Файл {file_path} был успешно удалён.")
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
            print(f"Папка {file_path} была успешно удалена.")
        else:
            print(f"Ошибка: {file_path} не является файлом или папкой.")
    except Exception as e:
        print(f"Произошла ошибка при удалении: {e}")
