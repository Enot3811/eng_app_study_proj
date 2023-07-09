"""A `Dataset` module.

The `Dataset` looks like below:
[
    {
        'word': 'str',
        'translates': [str, ...],
        'examples':
        [
            {
                'example_eng': str,
                'example_rus': str
            },
            {
                'example_eng': str,
                'example_rus': str
            },
            ...
        ]
    },
    {
        'word': 'str',
        'translates': [str, ...],
        'examples':
        [
            {
                'example_eng': str,
                'example_rus': str
            },
            {
                'example_eng': str,
                'example_rus': str
            },
            ...
        ]
    },
    ...
]

A `Dataset` object can take `str` or `int` as an index and then returns a dict
associated with the given word or index as described above.
"""

from pathlib import Path
import json
from typing import Dict, Union, List
import random


example_dict = Dict[str, str]
examples_list = List[example_dict]
translates_list = List[str]
sample_type = Dict[str, Union[str, translates_list, examples_list]]
samples_list = List[sample_type]


class Dataset:
    def __init__(self, dataset_path: Union[Path, str]) -> None:
        if isinstance(dataset_path, str):
            dataset_path = Path(dataset_path)
        if not dataset_path.exists():
            raise FileExistsError(
                f'The dataset file {dataset_path} does not exists.')
        with open(dataset_path, 'r') as f:
            data = f.read()
        self._samples: samples_list = json.loads(data)

        self._samples = list(sorted(self._samples,
                                    key=lambda sample: sample['word']))

        self._word_to_idx = {sample['word']: i
                             for i, sample in enumerate(self._samples)}

    def __len__(self) -> int:
        return len(self._samples)
    
    def __iter__(self) -> 'Dataset':
        self.iterator = iter(self._samples)
        self.iter_index = 0
        return self
    
    def __next__(self) -> sample_type:
        if self.iter_index <= len(self._samples):
            sample = next(self.iterator)
            self.iter_index += 1
            return sample
        else:
            raise StopIteration
            
    def __getitem__(self, index: Union[int, str]) -> sample_type:
        """Return a sample from this dataset by a word or a numeric index.

        Parameters
        ----------
        index : Union[int, str]
            Index for the sample getting.

        Returns
        -------
        sample_type
            The required sample.
        """
        if isinstance(index, str):
            index = self._word_to_idx[index]
        return self._samples[index]
    
    def __contains__(self, word: str) -> bool:
        """Check whether a given word is in this dataset.

        Parameters
        ----------
        word : str
            The word to check.

        Returns
        -------
        bool
            Whether the given word is in this dataset.
        """
        return word in self._word_to_idx
    
    def get_word_index(self, word: str) -> int:
        """Get an index of given word's sample in this dataset.

        Parameters
        ----------
        word : str
            The word whose index is to be obtained.

        Returns
        -------
        int
            The index of given word.
        """
        return self._word_to_idx[word]
    
    def random_choice(self, exclude: List[str] = None) -> sample_type:
        """Get a random sample from this dataset.

        Parameters
        ----------
        exclude : List[str], optional
            A list of words to avoid when getting a random sample.

        Returns
        -------
        sample_type
            The random sample.
        """
        indexes = list(range(len(self)))
        if exclude:
            for ex_word in exclude:
                indexes.pop(self._word_to_idx[ex_word])
        return self[random.choice(indexes)]
    
    def add_sample(
        self,
        word: str,
        translates: List[str],
        example_eng: str,
        example_rus: str
    ) -> None:
        """Add a given sample to this dataset.

        Parameters
        ----------
        word : str
            The word string of the sample.
        translates : List[str]
            A list of translates of the sample.
        example_eng : str
            An english example string of the sample.
        example_rus : str
            A russian example string of the sample.
        """
        self._samples.append(
            {'word': word,
             'translates': translates,
             'examples': [{
                 'example_eng': example_eng,
                 'example_rus': example_rus
             }]}
        )
        self._word_to_idx[word] = len(self._samples) - 1
        
    def save_dataset(self, save_path: Union[Path, str]):
        """Save this dataset to a json file.

        Parameters
        ----------
        save_path : Union[Path, str]
            A path for file saving.
        """
        if isinstance(save_path, str):
            save_path = Path(save_path)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        with open(save_path, 'w') as f:
            json.dump(self._samples, f, sort_keys=False,
                      indent=4, ensure_ascii=False)
