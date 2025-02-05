import sys
from commands.help import show_help
from commands.add_cat import add_cat
from commands.cats_list import cats_list
from commands.delete_folder import delete_folder
from commands.add_file import add_file


def main():
    if len(sys.argv) < 2:
        print("Не указана команда. Используйте 'help' для вывода списка команд.")
        return

    command = sys.argv[1]

    if command == "help":
        show_help()
    elif command == "add_cat":
        if len(sys.argv) < 3:
            print("Вы не ввели имя кота, пожалуйста, попробуйте снова")
            return
        cat_name = sys.argv[2]
        add_cat(cat_name)
    elif command == "cats_list":
        cats_list()
    elif command == "delete_folder":
        if len(sys.argv) < 3:
            print("Вы не ввели название папки, пожалуйста, попробуйте снова")
            return
        folder = sys.argv[2]
        delete_folder(folder)
    elif command == "add_file":
        if len(sys.argv) < 3:
            print("Вы не ввели путь файла и(ли) папку назначения, пожалуйста, попробуйте снова")
            return
        add_file(sys.argv[2], sys.argv[3])
    else:
        print(f"Неизвестная команда: {command}. Используйте 'help' для вывода списка команд.")


if __name__ == "__main__":
    main()
