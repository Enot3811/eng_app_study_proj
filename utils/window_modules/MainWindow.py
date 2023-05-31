from pathlib import Path
from typing import Tuple
import sys

from PySide6.QtWidgets import QMainWindow

sys.path.append(Path(__file__).parents[2])
from utils.ui_modules import Ui_MainWindow
from utils.database_utils import Dataset, sample_type


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, dataset: Dataset) -> None:
        super().__init__()
        self.setupUi(self)
        self.dataset = dataset
        # A current sample is represented as a sample dict type
        # and an int index of a current selected example
        # When current example is changed, this int index will be changed too
        self.current_sample = (self.dataset.random_choice(), 0)
        self._show_sample(self.current_sample)

    def _show_sample(self, sample: Tuple[sample_type, int]):
        """Show a given sample on this form.

        Parameters
        ----------
        sample : Tuple[sample_type, int]
            The sample to show.
        """
        sample, example_idx = sample
        word = sample['word']
        translates = sample['translates']
        examples = sample['examples']

        self.wordLineEdit.setText(word.capitalize())
        self.translateTextEdit.setText(', '.join(translates).capitalize())
        self.engExampleTextEdit.setText(examples[example_idx]['example_eng'])
        self.rusExampleTextEdit.setText(examples[example_idx]['example_rus'])
