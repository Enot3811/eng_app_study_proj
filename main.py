from pathlib import Path
import sys
from typing import List, Tuple

import PySimpleGUI as sg

from dataset import Dataset, Example, Sample


DEFAULT_PATH = Path(sys.argv[0]).parent / 'words.json'


def make_main_window(text_size: int = 70) -> sg.Window:
    layout = [
        [sg.Frame('Word', [
            [sg.Input(key='word', size=(text_size, 1),
                      pad=(5, (10, 5)), disabled=True)],
            [sg.Multiline(key='translates',
                          size=(text_size, 2), disabled=True)]
        ], font=16)],
        [sg.Frame('Examples', [
            [sg.Multiline(key='example_eng',
                          size=(text_size, 4),
                          pad=(5, (10, 5)),
                          disabled=True)],
            [sg.Multiline(key='example_rus',
                          size=(text_size, 4),
                          disabled=True)],
            [
                sg.Column([[sg.Button('<<<')]]),
                sg.Column([[sg.Button('Drop example')]], justification='c'),
                sg.Column([[sg.Button('Add example')]], justification='c'),
                sg.Column([[sg.Button('>>>')]])
            ]], font=16)],
        [sg.Button('Edit sample'), sg.Button('Add sample'), sg.Button('Next')]]
    return sg.Window(
        'Eng app', layout, finalize=True, element_padding=(5, 5), font=14)


def make_sample_window(text_size: int = 70) -> sg.Window:
    layout = [
        [sg.Frame('Word', [
            [sg.Input(key='word', size=(text_size, 1), pad=(5, (10, 5)))],
            [sg.Multiline(key='translates', size=(text_size, 2))]
        ], font=16)],
        [sg.Frame('Examples', [
            [sg.Multiline(key='example_eng',
                          size=(text_size, 4),
                          pad=(5, (10, 5)))],
            [sg.Multiline(key='example_rus',
                          size=(text_size, 4))]
        ], font=16)],
        [sg.Column([[sg.Button('Add sample')]], justification='c')]]
    return sg.Window(
        'Eng app', layout, finalize=True, element_padding=(5, 5), font=14)


def get_new_random_sample(current_sample: Sample, dataset: Dataset) -> Sample:
    """
    Get a new random sample from the dataset.

    Parameters
    ----------
    current_sample : Sample
        A current sample.
    dataset : Dataset
        The dataset.

    Returns
    -------
    Sample
        The new sample from the dataset.
    """
    # Iterate while word of current and gotten sample is equal.
    # It is need to avoid returning of the same sample.
    while True:
        sample = dataset.random_choice()
        if sample.word != current_sample.word:
            break
    return sample


def update_sample(window: sg.Window, sample: Sample) -> None:
    """
    Show a given sample on a given window.

    Parameters
    ----------
    window : sg.Window
        The window that shows samples.
    sample : Sample
        The sample to show.
    """
    sample.word
    window['word'].update(sample.word.title())
    window['translates'].update(', '.join(sample.translates).title())
    update_example(window, sample.examples)


def update_example(window: sg.Window, examples: Example, index: int = 0):
    """
    Load a new example of a sample on a given window.

    Parameters
    ----------
    window : sg.Window
        The window that shows samples.
    examples : Example
        The examples of the sample.
    index : int, optional
        An index of the example.
    """
    window['example_eng'].update(examples[index].eng)
    window['example_rus'].update(examples[index].rus)


def parse_input(
    word: str, translate: str, example_eng: str, example_rus: str
) -> Tuple[str, List[str], str, str]:
    """
    Parse input strings. Split a translate string into words,
    set all characters to lower case.

    Parameters
    ----------
    word : str
        The word string.
    translate : str
        The translate string.
    example_eng : str
        The english example string.
    example_rus : str
        The russian example string.

    Returns
    -------
    Tuple[str, List[str], str, str]
        Parsed input strings
    """
    word = word.lower()
    translate = translate.lower().replace(',', '').split()
    return word, translate, example_eng, example_rus
    

def main():
    dataset = Dataset(DEFAULT_PATH)
    main_window = make_main_window()
    current_sample = dataset.random_choice()
    update_sample(main_window, current_sample)
    example_index = 0

    while True:
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED and window == main_window:
            break

        if window == main_window:
            # Exit
            if event == sg.WIN_CLOSED:
                break
            # Main sample
            if event == 'Next':
                current_sample = get_new_random_sample(current_sample, dataset)
                update_sample(main_window, current_sample)
                example_index = 0
            elif event == '>>>':
                example_index = (
                    (example_index + 1) % len(current_sample.examples))
                update_example(
                    main_window, current_sample.examples, example_index)
            elif event == '<<<':
                example_index = (
                    (example_index - 1) % len(current_sample.examples))
                update_example(
                    main_window, current_sample.examples, example_index)
            # Go to sample
            elif event == 'Add sample':
                main_window.hide()
                sample_window = make_sample_window()
        elif window == sample_window:
            # Go to main
            if event == sg.WIN_CLOSED:
                sample_window.close()
                main_window.UnHide()
            # Sample
            elif event == 'Add sample':
                word = values['word']
                translates = values['translates']
                example_eng = values['example_eng']
                example_rus = values['example_rus']
                word, translates, example_eng, example_rus = parse_input(
                    word, translates, example_eng, example_rus
                )
                if not dataset.add_sample(word, translates, example_eng,
                                          example_rus):
                    sg.popup_ok(f'The dataset has already the word "{word}".')
                # Go to main
                else:
                    sample_window.close()
                    main_window.UnHide()
                    sample = dataset[word]
                    update_sample(main_window, sample)

    dataset.save_dataset(DEFAULT_PATH)
    main_window.close()


if __name__ == '__main__':
    main()
