from pathlib import Path
import sys

from PySide6.QtWidgets import QMainWindow

sys.path.append(Path(__file__).parents[2])
from utils.ui_modules.MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
