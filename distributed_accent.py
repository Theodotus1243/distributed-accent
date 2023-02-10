from typing import List
from ukrainian_word_stress import Stressifier, StressSymbol, OnAmbiguity
import numpy as np

import hashlib



def hash_file(filename: str, block_size: int=2**20):
    md5 = hashlib.md5()
    with open(filename, "rb") as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            md5.update(data)
    return md5.digest()


def stress(texts: List[str]):
    ambiguous_texts = []
    stressify_skip = Stressifier(stress_symbol=StressSymbol.CombiningAcuteAccent, on_ambiguity = OnAmbiguity.Skip)
    stressify_all = Stressifier(stress_symbol=StressSymbol.CombiningAcuteAccent, on_ambiguity = OnAmbiguity.All)
    for text in texts:
        text_skip = stressify_skip(text)
        text_all = stressify_all(text)
        ambiguity = (text_skip!=text_all)
        ambiguous_texts.append((text_all, ambiguity))
    return ambiguous_texts


if (__name__ == "__main__"):
    filename = "full.txt"


    # check integrity
    assert hash_file(filename) == b'=\x9e\x1f\xec\xa6\x81\xc1\xd84\xbd\x0b?.\x1b\x8ew'
    num_lines = 58070492


    # get chunk of data
    