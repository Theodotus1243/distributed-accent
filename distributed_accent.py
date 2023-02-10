from typing import List
from ukrainian_word_stress import Stressifier, StressSymbol, OnAmbiguity
import numpy as np



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
