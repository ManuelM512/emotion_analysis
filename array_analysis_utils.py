from emotion_dicts import palabras_negativas, palabras_neutras, palabras_positivas
import numpy as np


def mean_quality(w):
    total_keywords = (
        len(palabras_positivas) + len(palabras_negativas) + len(palabras_neutras)
    )
    amount_key = sum(w)
    return amount_key / total_keywords


def mean_emotion(s):
    return np.multiply(s, np.array([1, 0, -1]))


def each_emotion_mean(s):
    total = sum(s)
    if total != 0:
        positive = s[0] / total
        neutral = s[1] / total
        negative = s[2] / total
        return positive, neutral, negative
    return 0, 0, 0
