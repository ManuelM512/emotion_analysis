from word_analysis import sentimental_array
from string_sanitization import sanitize_phrase
from phrases import phrases_list
from text_utils import write_to_file
from array_analysis_utils import mean_emotion, mean_quality, each_emotion_mean


def main():
    list_to_print = ["Frase,Calidad,Positivo,Neutro,Negativo,Promedio de emoción,s,w"]
    for phrase in phrases_list:
        sanitized = sanitize_phrase(phrase)
        s, w = sentimental_array(sanitized.split(" "))
        quality = mean_quality(w)
        emotion = mean_emotion(s)
        positive, neutral, negative = each_emotion_mean(s)
        list_to_print.append(
            f'"{phrase}",{quality},{positive},{neutral},{negative},{emotion},{s},{w}'
        )
    write_to_file("phrase_with_arrays.csv", list_to_print)


if __name__ == "__main__":
    main()
