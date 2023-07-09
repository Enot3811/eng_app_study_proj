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
        self.page_idxs = {
            'main': 0,
            'add_sample': 1
        }
        self.stackedWidget.setCurrentIndex(self.page_idxs['main'])
        self._setup_handlers()
        self.dataset = dataset

        # Service variables
        self._current_sample: sample_type = self.dataset.random_choice()
        self._current_example = 0

        # Set up main page
        self._show_sample(self._current_sample)

    def _setup_handlers(self):
        """Setup event handlers connections."""
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
        self.toAddSampleButton.clicked.connect(
            self._to_add_sample_button_click)
        self.fromAddToMainPushButton.clicked.connect(
            self._from_add_to_main_button_click)

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
        current_idx = self.dataset.get_word_index(self._current_sample['word'])
        current_idx = (current_idx + 1) % len(self.dataset)
        sample = self.dataset[current_idx]
        self._show_sample(sample)
        self._current_sample = sample

    def _previous_sample_button_click(self):
        current_idx = self.dataset.get_word_index(self._current_sample['word'])
        current_idx = (current_idx - 1) % len(self.dataset)
        sample = self.dataset[current_idx]
        self._show_sample(sample)
        self._current_sample = sample

    def _random_sample_button_click(self):
        current_word = self._current_sample['word']
        sample = self.dataset.random_choice([current_word])
        self._show_sample(sample)
        self._current_sample = sample

    def _right_example_button_click(self):
        examples = self._current_sample['examples']
        self._current_example = (self._current_example + 1) % len(examples)
        self._show_example(examples[self._current_example])

    def _left_example_button_click(self):
        examples = self._current_sample['examples']
        self._current_example = (self._current_example - 1) % len(examples)
        self._show_example(examples[self._current_example])

    def _to_add_sample_button_click(self):
        self.successful_save_label.setVisible(False)
        self.stackedWidget.setCurrentIndex(self.page_idxs['add_sample'])

    def _from_add_to_main_button_click(self):
        self.stackedWidget.setCurrentIndex(self.page_idxs['main'])

    def closeEvent(self, close_event):
        self.dataset.save_dataset(Path(sys.argv[0]).parent / 'words.json')
