from pathlib import Path

import PySimpleGUI as sg

from dataset import Dataset


DEFAULT_PATH = Path(__file__).parent.absolute() / 'Dictionary' / 'words.json'


def load_dictionary(path: Path = DEFAULT_PATH) -> Dataset:
    """Load a dictionary database.

    Parameters
    ----------
    path : Path, optional
        A path to database json.

    Returns
    -------
    Dataset
        A dataset of words.
    """
    if path.exists():
        return Dataset(path)


def make_main_window(dataset: Dataset) -> sg.Window:
    sample = dataset.random_choice()
    layout = [
        [sg.Text(sample.word, key='word')],
        [sg.Text(', '.join(sample.translates), key='translates')],
        [sg.Text(sample.examples[0].eng, key='example_eng')],
        [sg.Text(sample.examples[0].rus, key='example_rus')],
        [sg.Button('Next')]]
    return sg.Window('Eng app', layout, finalize=True)


def make_sample_window() -> sg.Window:
    layout = [
        [sg.Text('There will be some content.')],
        [sg.Button('Next')]]
    return sg.Window('Sample', layout, finalize=True)


def update_sample(window: sg.Window, dataset: Dataset) -> Sample:
    """
    Show a new random sample on a given window.

    Parameters
    ----------
    window : sg.Window
        The window that shows samples.
    dataset : Dataset
        A dataset of words.

    Returns
    -------
    Sample
        The showed sample.
    """
    while True:
        sample = dataset.random_choice()
        if sample.word != window['word'].get():
            break
    window['word'].update(sample.word)
    window['translates'].update(', '.join(sample.translates))
    window['example_eng'].update(sample.examples[0].eng)
    window['example_rus'].update(sample.examples[0].rus)


def main():
    dataset = load_dictionary()

    sg.theme('DarkAmber')
    main_window = make_main_window(dataset)

    while True:
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED and window == main_window:
            break

        if window == main_window:
            # Sample
            if event == 'Next':
                update_sample(main_window, dataset)

    main_window.close()


if __name__ == '__main__':
    main()
