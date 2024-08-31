from word_analysis import sentimental_array
from string_sanitization import sanitize_phrase
from phrases import phrases_list
from text_utils import write_to_file


def main():
    list_to_print = []
    for phrase in phrases_list:
        sanitized = sanitize_phrase(phrase)
        s, w = sentimental_array(sanitized.split(" "))
        list_to_print.append(f"{phrase};{s};{w}")
    write_to_file("phrase_with_arrays.txt", list_to_print)


if __name__ == "__main__":
    main()
