## Análisis sentimental

El archivo `main.py` se encargará de llamar a todas las demás funciones del proyecto. Su función principal es analizar una lista de frases, procesarlas, y generar un archivo CSV con los resultados del análisis. A continuación, se describen los pasos que realiza:

1. **Sanitización de la Frase:** Utiliza la función `sanitize_phrase` para limpiar y preparar la frase para el análisis.
2. **Construcción de Vectores:** Emplea `sentimental_array` para crear los vectores `s` y `w` que representan la presencia de palabras clave y el conteo de palabras positivas, neutrales y negativas.
3. **Cálculo de Métricas:** Calcula la calidad promedio (`mean_quality`), el sentimiento promedio (`mean_emotion`), y la distribución de sentimientos (`each_emotion_mean`) para cada frase.
4. **Generación del Archivo CSV:** Finalmente, escribe los resultados de este análisis en un archivo CSV llamado `phrase_with_arrays.csv` utilizando `write_to_file`.

Este archivo CSV incluye la frase original, su calidad, el porcentaje de palabras positivas, neutrales y negativas, el promedio de emoción, y los vectores `s` y `w` generados.

<br>
En los archivos `phrases_list` y `emotion_dicts` se pueden encontrar una lista de frases y los 3 diccionarios para cada grupo de palabras claves. El valor de cada par clave-valor se utilizó para poder generar el vector `w` que necesitaba que se respetara un lugar para cada palabra. 

## Ejecución

Para ejecutar el análisis, simplemente corre el archivo `main.py` en tu entorno de desarrollo:

```bash
python main.py
```

Esto generará un archivo `phrase_with_arrays.csv` en el directorio actual con el resultado del análisis de las frases.
