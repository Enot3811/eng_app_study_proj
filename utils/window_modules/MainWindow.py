from pathlib import Path
import sys

from PySide6.QtWidgets import QMainWindow

sys.path.append(Path(__file__).parents[2])
from utils.ui_modules import Ui_MainWindow
from utils.database_utils import Dataset, sample_type, example_dict


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, dataset: Dataset) -> None:
        super().__init__()
        self.setupUi(self)
        self._setup_handlers()
        self.dataset = dataset
        self.current_sample: sample_type = self.dataset.random_choice()
        self.current_example = 0
        self._show_sample(self.current_sample)

    def _setup_handlers(self):
        self.rightExampleButton.clicked.connect(
            self._right_example_button_click)
        self.leftExampleButton.clicked.connect(
            self._left_example_button_click)
        self.randomSampleButton.clicked.connect(
            self._random_sample_button_click)
        self.nextSampleButton.clicked.connect(
            self._next_sample_button_click)
        self.previousSampleButton.clicked.connect(
            self._previous_sample_button_click)

    def _show_sample(self, sample: sample_type, example_idx: int = 0):
        """Show a given sample on this form.

        Parameters
        ----------
        sample : Tuple[sample_type, int]
            The sample to show.
        example_idx : int, optional
            An index of sample's example to show. By default is equal 0.
        """
        word = sample['word']
        translates = sample['translates']
        examples = sample['examples']

        self.wordLineEdit.setText(word.capitalize())
        self.translateTextEdit.setText(', '.join(translates).capitalize())
        self._show_example(examples[example_idx])

    def _show_example(self, example: example_dict):
        """Show a given example on this form.

        Parameters
        ----------
        example : example_dict
            The example to show.
        """
        self.engExampleTextEdit.setText(example['example_eng'])
        self.rusExampleTextEdit.setText(example['example_rus'])

    def _next_sample_button_click(self):
        current_idx = self.dataset.get_word_index(self.current_sample['word'])
        current_idx = (current_idx + 1) % len(self.dataset)
        sample = self.dataset[current_idx]
        self._show_sample(sample)
        self.current_sample = sample

    def _previous_sample_button_click(self):
        current_idx = self.dataset.get_word_index(self.current_sample['word'])
        current_idx = (current_idx - 1) % len(self.dataset)
        sample = self.dataset[current_idx]
        self._show_sample(sample)
        self.current_sample = sample

    def _random_sample_button_click(self):
        current_word = self.current_sample['word']
        sample = self.dataset.random_choice([current_word])
        self._show_sample(sample)
        self.current_sample = sample

    def _right_example_button_click(self):
        examples = self.current_sample['examples']
        self.current_example = (self.current_example + 1) % len(examples)
        self._show_example(examples[self.current_example])

    def _left_example_button_click(self):
        examples = self.current_sample['examples']
        self.current_example = (self.current_example - 1) % len(examples)
        self._show_example(examples[self.current_example])
