from pathlib import Path
import sys

from PySide6.QtWidgets import QMainWindow, QSizePolicy

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

        # Set up add sample page
        self.add_sample_msgs_labels = [
            self.newWordMsgLabel, self.newWordTranslateMsgLabel,
            self.newWordExampleEngMsgLabel, self.newWordExampleRusMsgLabel]
        success_label_policy = QSizePolicy()
        success_label_policy.setRetainSizeWhenHidden(True)
        self.successful_save_label.setSizePolicy(success_label_policy)

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
        self.saveNewSampleButton.clicked.connect(
            self._save_new_sample_button_click)
        self.clearAddSamplePageButton.clicked.connect(
            self._clear_add_sample_page)

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

    def _clear_add_sample_page(self):
        for label in self.add_sample_msgs_labels:
            label.setStyleSheet('QLabel { font-size: 12pt; color : black; }')
        for text_input in [self.newWordLineEdit,
                           self.newWordTranslateTextEdit,
                           self.newWordExampleEngTextEdit,
                           self.newWordExampleRusTextEdit]:
            text_input.clear()
        self.successful_save_label.setVisible(False)
        
    def _to_add_sample_button_click(self):
        self._clear_add_sample_page()
        self.stackedWidget.setCurrentIndex(self.page_idxs['add_sample'])

    def _from_add_to_main_button_click(self):
        self.stackedWidget.setCurrentIndex(self.page_idxs['main'])

    def _save_new_sample_button_click(self):
        word = self.newWordLineEdit.text()
        translate = self.newWordTranslateTextEdit.toPlainText()
        example_eng = self.newWordExampleEngTextEdit.toPlainText()
        example_rus = self.newWordExampleRusTextEdit.toPlainText()
        
        correct = True
        for text, label in zip([word, translate, example_eng, example_rus],
                               self.add_sample_msgs_labels):
            if text.isspace() or text == '':
                label.setStyleSheet('QLabel { font-size: 12pt; color : red; }')
                correct = False
            else:
                label.setStyleSheet(
                    'QLabel { font-size: 12pt; color : black; }')
        
        if correct:
            word = word.strip().capitalize()
            self.newWordLineEdit.setText(word)
            word = word.lower()
            translate = translate.strip()
            self.newWordTranslateTextEdit.setText(translate)
            translate = [trans.strip().lower()
                         for trans in translate.split(',')]
            example_eng = example_eng.strip()
            self.newWordExampleEngTextEdit.setText(example_eng)
            example_rus = example_rus.strip()
            self.newWordExampleRusTextEdit.setText(example_rus)

            self.dataset.add_sample(word, translate, example_eng, example_rus)
            self.successful_save_label.setVisible(True)
            # Show new sample on main page
            self._current_sample = self.dataset[word]
            self._show_sample(self._current_sample)

    def closeEvent(self, close_event):
        self.dataset.save_dataset(Path(sys.argv[0]).parent / 'words.json')
