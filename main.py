from pathlib import Path

import PySimpleGUI as sg

from dataset import Dataset, Example, Sample


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
        [sg.Button('Edit sample'), sg.Button('Next')]]
    return sg.Window(
        'Eng app', layout, finalize=True, element_padding=(5, 5), font=14)


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
    update_example(window, sample.examples)
    return sample


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


def main():
    dataset = load_dictionary()
    main_window = make_main_window()
    current_sample = update_sample(main_window, dataset)
    example_index = 0

    while True:
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED and window == main_window:
            break

        if window == main_window:
            # Sample
            if event == 'Next':
                current_sample = update_sample(main_window, dataset)
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

    main_window.close()


if __name__ == '__main__':
    main()
