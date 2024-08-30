import numpy as np

from emotion_dicts import palabras_negativas, palabras_neutras, palabras_positivas


def sum_words(s, w, word):
    if word in palabras_positivas:
        s[0] += 1
        w[palabras_positivas[word]] += 1
    elif word in palabras_neutras:
        s[1] += 1
        w[palabras_neutras[word]] += 1
    elif word in palabras_negativas:
        s[2] += 1
        w[palabras_negativas[word]] += 1


def sentimental_array(phrase):
    w = np.array([0] * 30)
    s = np.array([0, 0, 0])
    for word in phrase:
        sum_words(s, w, word)
    return s, w
