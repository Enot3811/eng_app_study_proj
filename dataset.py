from pathlib import Path
import json
from typing import Dict, Union, List
from collections import namedtuple
import random

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
