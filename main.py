from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication

sys.path.append(Path(__file__).parent)
from utils.window_modules import MainWindow
from utils.database_utils import Dataset


def main():
    application = QApplication()
    dataset = Dataset('words.json')
    main_window = MainWindow(dataset)
    main_window.show()
    application.exec()


if __name__ == '__main__':
    main()
