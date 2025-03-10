from PySide6 import QtWidgets
import sys
import os
from commands._get_cat_folder_path import get_cat_folder_path
from commands.add_cat import add_cat
from commands.add_file import add_file
from commands.delete_file import delete_file


def _make_full_path(item):
    if item.parent() is None:
        return [item.text(0)]
    return _make_full_path(item.parent()) + [item.text(0)]


class FelineManagerGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Feline Manager")
        self.resize(400, 300)

        # Выбор инструмента
        self.tool_label = QtWidgets.QLabel("Выберите инструмент:")
        self.tool_combo = QtWidgets.QComboBox()
        self.tool_combo.addItems(
            ["Добавить кота", "Добавить файл в папку кота", "Удалить файл или папку"])

        # Выбор файла
        self.file_label = QtWidgets.QLabel("Файл не выбран")
        self.file_button = QtWidgets.QPushButton("Выбрать файл")
        self.file_button.clicked.connect(self.select_file)

        # Кнопка запуска
        self.run_button = QtWidgets.QPushButton("Запустить")
        self.run_button.clicked.connect(self.run_tool)

        # Текущий список файлов
        self.file_tree = QtWidgets.QTreeWidget()
        self.file_tree.setHeaderLabels(["Коты и их файлы"])
        self.update_file_tree()

        # Лог выполнения
        self.log_output = QtWidgets.QTextEdit()
        self.log_output.setReadOnly(True)

        # Компоновка
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.tool_label)
        layout.addWidget(self.tool_combo)
        layout.addWidget(self.file_label)
        layout.addWidget(self.file_button)
        layout.addWidget(self.run_button)
        layout.addWidget(self.file_tree)
        layout.addWidget(self.log_output)
        self.setLayout(layout)

    def update_file_tree(self):
        def make_item_in_tree(full_path):
            item_in_tree = QtWidgets.QTreeWidgetItem([os.path.basename(full_path)])
            if os.path.isdir(full_path):
                for subpath in os.listdir(full_path):
                    child_item = make_item_in_tree(os.path.join(full_path, subpath))
                    item_in_tree.addChild(child_item)
            return item_in_tree

        base_dir, cats_dir, cat_name_dir = get_cat_folder_path('')
        top_level_item = make_item_in_tree(cats_dir)

        top_level = self.file_tree.takeTopLevelItem(0)
        del top_level
        self.file_tree.insertTopLevelItems(0, [top_level_item])

    def select_file(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Выбрать файл")
        if file_path:
            self.file_label.setText(file_path)

    def run_tool(self):
        available_tools_mapping = {"Добавить кота": self.process_add_cat,
                                   "Добавить файл в папку кота": self.process_add_file,
                                   "Удалить файл или папку": self.process_delete
                                   }
        tool = self.tool_combo.currentText()

        available_tools_mapping[tool]()

        self.update_file_tree()

    def process_add_cat(self):
        cat_name, is_ok = QtWidgets.QInputDialog.getText(self, "Новый котек))", "Введите имя нового котека))))")
        if not is_ok:
            self.log_output.append("Отмена добавления котека")
            return
        add_cat(cat_name)

    def process_add_file(self):
        file_path = self.file_label.text()
        selected_items = self.file_tree.selectedItems()

        if len(selected_items) == 0:
            self.log_output.append("Выберите котека, куда положить файл")
            return
        if len(selected_items) > 1:
            self.log_output.append("Выберите ровно одного котека, куда положить файл")
            return
        if file_path == "Файл не выбран":
            self.log_output.append("Надо выбрать файл")
            return

        path_to_selected_item = os.path.join(*_make_full_path(selected_items[0])[1:])

        if not os.path.isdir(path_to_selected_item):
            self.log_output.append("Надо выбрать папку")

        add_file(file_path, path_to_selected_item)

    def process_delete(self):
        selected_items = self.file_tree.selectedItems()
        if len(selected_items) == 0:
            self.log_output.append("Не выбран файл или папка для удаления")
        if len(selected_items) >= 2:
            self.log_output.append("Удалять файлы или папки можно только по одному")

        item_to_delete = os.path.join(*_make_full_path(selected_items[0]))
        delete_file(item_to_delete)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FelineManagerGUI()
    window.show()
    sys.exit(app.exec())
