from pathlib import Path
import json
from typing import Dict, Union, List
from collections import namedtuple
import random

# Dicts like in words.json
SampleDict = Dict[str, Union[List[str], Dict[str, str]]]
DataDict = Dict[str, SampleDict]

Sample = namedtuple('Sample', ['word', 'translates', 'examples'])
Example = namedtuple('Example', ['eng', 'rus'])


class Dataset:
    """
    A dataset of words. Consists of `SampleDict` objects, that include
    an english word, its translate and some example sentences.
    """
    def __init__(self, dataset_path: Path) -> None:
        if not dataset_path.exists():
            raise FileExistsError(
                f'The dataset file {dataset_path} does not exists.')
        
        with open(dataset_path, 'r') as f:
            data = f.read()
        self.samples: DataDict = json.loads(data)

    def __len__(self) -> int:
        return len(self.samples)
            
    def __getitem__(self, word: str) -> SampleDict:
        return self.samples[word]
    
    def random_choice(self) -> Sample:
        """Get random sample from dataset.

        Returns
        -------
        Sample
            A tuple consists of a english word, its translates
            and some example sentences.
        """
        word = random.choice(list(self.samples.keys()))
        sample_dict = self[word]
        translates = sample_dict['translates']
        examples = [Example(eng, rus)
                    for eng, rus in sample_dict['examples'].items()]
        return Sample(word, translates, examples)
    
    def add_sample(
        self,
        word: str,
        translates: List[str],
        example_eng: str,
        example_rus: str
    ) -> bool:
        """
        Add a given sample to a dataset if the dataset does not already have
        the same word.

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

        Returns
        -------
        bool
            Whether the given sample is added to the dataset.
        """
        if self.samples.get(word, False):
            return False
        else:
            self.samples[word] = {
                "translates": translates,
                "examples": {
                    example_eng: example_rus
                }
            }
            return True
