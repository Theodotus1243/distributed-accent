from typing import List
from ukrainian_word_stress import Stressifier, StressSymbol, OnAmbiguity
from tqdm import tqdm
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


def get_chunk_indices(start: int, end: int):
    line_indices = np.arange(num_lines)
    np.random.shuffle(line_indices)

    chunks = np.array_split(line_indices, total_chunks)
    selected_chunks_list = chunks[start: end]
    selected_chunks = np.concatenate(selected_chunks_list)
    return selected_chunks


def read_chunks(filename: str, chunk_indices: np.array):
    chunk_indices_set = set(chunk_indices)
    with open(filename) as file:
        print("Reading chunks")
        chunk_text = [sentence for idx, sentence in tqdm(enumerate(file), total=num_lines) if (idx in chunk_indices_set)]
        
    assert len(chunk_text) == len(chunk_indices)

    return chunk_text


if (__name__ == "__main__"):
    filename = "full.txt"
    start = 0
    end = 100


    # check integrity
    assert hash_file(filename) == b'=\x9e\x1f\xec\xa6\x81\xc1\xd84\xbd\x0b?.\x1b\x8ew'
    num_lines = 58070492
    total_chunks = 1000


    # set seed
    seed = 42
    np.random.seed(seed)


    # get chunk of data
    chunk_indices = get_chunk_indices(start, end)

    chunk_text = read_chunks(filename, chunk_indices)