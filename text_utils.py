def write_to_file(nombre_archivo, lineas):
    with open(nombre_archivo, "w") as archivo:
        for linea in lineas:
            archivo.write(linea + "\n")
