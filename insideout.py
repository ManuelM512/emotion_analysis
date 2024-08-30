from word_analysis import sentimental_array
from string_sanitization import sanitize_phrase
from phrases import phrases_list


def escribir_linea_a_archivo(nombre_archivo, lineas):
    with open(nombre_archivo, "w") as archivo:
        for linea in lineas:
            archivo.write(linea + "\n")


def main():
    sanitized = []
    for phrase in phrases_list:
        sanitized.append(sanitize_phrase(phrase))


if __name__ == "__main__":
    main()
