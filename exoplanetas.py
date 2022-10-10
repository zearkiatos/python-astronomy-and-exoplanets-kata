from cmath import cos, isnan, sin
from dis import disco
from turtle import color, title
import pandas as pd
import matplotlib.pyplot as plt
import math as m
import numpy as np
import statistics
import math

plt.rcParams.update({'font.size': 12})


def cargar_datos(nombre_archivo: str) -> pd.DataFrame:
    """ Carga los datos de un archivo csv y retorna el DataFrame con la informacion.
    Parametros:
        nombre_archivo (str): El nombre del archivo CSV que se debe cargar
    Retorno:
        (DataFrame) : El DataFrame con todos los datos contenidos en el archivo
    """
    data = pd.read_csv(nombre_archivo)

    return data


def histograma_descubrimiento(datos: pd.DataFrame) -> None:
    """ Calcula y despliega un histograma con 30 grupos (bins) en el que debe
        aparecer la cantidad de planetas descubiertos por anho.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    discovery = datos["DESCUBRIMIENTO"]
    ax = discovery.plot(
        kind="hist", bins=30, title="Cantidad de planetas descubiertos entre 1988 y 2018")

    ax.set_xlabel("Años", fontsize=9)

    ax.set_ylabel("Cantidad de planetas descubiertos", fontsize=9)

    figure = ax.get_figure()

    figure.savefig('./assets/histogram.png')
    plt.show()
    pass


def estado_publicacion_por_descubrimiento(datos: pd.DataFrame) -> None:
    """ Calcula y despliega un BoxPlot donde aparecen la cantidad de planetas
        descubiertos por anho, agrupados de acuerdo con el tipo de publicacion.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """

    ax = datos[["DESCUBRIMIENTO", "ESTADO_PUBLICACION"]].boxplot(
        by="ESTADO_PUBLICACION", figsize=(9, 30))

    ax.set_ylabel("Año de descubrimiento")

    ax.set_title("Tipo de publicación vs año de descubrimiento")

    figure = ax.get_figure()

    figure.savefig('./assets/boxplot.png')
    plt.show()

    pass


def deteccion_por_descubrimiento(datos: pd.DataFrame) -> None:
    """ Calcula y despliega un BoxPlot donde aparecen la cantidad de planetas
        descubiertos por anho, agrupados de acuerdo con el tipo de deteccion
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    ax = datos[["DESCUBRIMIENTO", "TIPO_DETECCION"]].boxplot(
        by="TIPO_DETECCION", figsize=(9, 9))

    ax.set_ylabel("Año de descubrimiento")

    ax.set_title("Tipo de detección vs año de descubrimiento")

    figure = ax.get_figure()

    figure.savefig('./assets/boxplot-tipo-deteccion.png')
    plt.show()

    pass


def deteccion_y_descubrimiento(datos: pd.DataFrame, anho: int) -> None:
    """ Calcula y despliega un diagrama de pie donde aparecen la cantidad de
        planetas descubiertos en un anho particular, clasificados de acuerdo
        con el tipo de publicacion.
        Si el anho es 0, se muestra la información para todos los planetas.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
        anho (int): el anho para el que se quieren analizar los planetas descubiertos
                    o 0 para indicar que deben ser todos los planetas.
    """
    name = ''
    if anho == 0:
        data = datos[["DESCUBRIMIENTO", "TIPO_DETECCION"]
                     ]
        name = "pie-tipo-deteccion"
    else:
        data = datos[["DESCUBRIMIENTO", "TIPO_DETECCION"]]
        data = data[data["DESCUBRIMIENTO"] == anho]
        name = "pie-tipo-deteccion-"+str(anho)

    data.groupby(["TIPO_DETECCION"]).sum().plot(
        kind="pie", y="DESCUBRIMIENTO", autopct='%1.0f%%', legend=False)

    plt.savefig("./assets/"+name+".png")

    plt.show()

    pass


def fix_nan(nan) -> int:
    result = nan
    if (np.isnan(nan)):
        result = 0

    return result


def quit_nan(nan) -> any:
    result = nan
    if type(nan) is list:
        return nan
    if (np.isnan(nan)):
        result = 0
    return result


def average(array) -> any:
    result = array
    if type(array) is list:
        return statistics.mean(array)
    return result


def cantidad_y_tipo_deteccion(datos: pd.DataFrame) -> None:
    """ Calcula y despliega un diagrama de lineas donde aparece una linea por
        cada tipo de deteccion y se muestra la cantidad de planetas descubiertos
        en cada anho, para ese tipo de deteccion.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    dictionaries = datos.to_dict('records')
    data_reordered = {}

    for dictionary in dictionaries:
        if (not dictionary['TIPO_DETECCION'] in list(data_reordered)):
            data_reordered[dictionary['TIPO_DETECCION']] = {}
            data_reordered[dictionary['TIPO_DETECCION']
                           ][dictionary['DESCUBRIMIENTO']] = 1
        else:
            if (not dictionary['DESCUBRIMIENTO'] in list(data_reordered[dictionary['TIPO_DETECCION']])):
                data_reordered[dictionary['TIPO_DETECCION']
                               ][int(dictionary['DESCUBRIMIENTO'])] = 1
            else:
                data_reordered[dictionary['TIPO_DETECCION']
                               ][int(dictionary['DESCUBRIMIENTO'])] += 1

    for data in data_reordered:
        data_reordered[data] = pd.Series(data_reordered[data])

    dataframe_dictionary = pd.DataFrame(data_reordered)

    for data in data_reordered:
        dataframe_dictionary[data] = dataframe_dictionary[data].apply(fix_nan)
        dataframe_dictionary[data] = dataframe_dictionary[data].apply(
            lambda x: int(x))

    plt.plot(dataframe_dictionary)
    plt.title("Cantidad de planetas descubiertos según el tipo de detección")
    plt.xlabel("Año de descubrimiento")
    plt.ylabel("Cantidad de planetas descubiertos")
    plt.legend(list(data_reordered))

    plt.savefig('./assets/histogram-discovery-quantity.png')

    plt.show()

    pass


def masa_promedio_y_tipo_deteccion(datos: pd.DataFrame) -> None:
    """ Calcula y despliega un diagrama de lineas donde aparece una linea por
        cada tipo de detección y se muestra la masa promedio de los planetas descubiertos
        en cada anho, para ese tipo de deteccion.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    dictionaries = datos.to_dict('records')
    data_reordered = {}

    for dictionary in dictionaries:
        if (not dictionary['TIPO_DETECCION'] in list(data_reordered)):
            data_reordered[dictionary['TIPO_DETECCION']] = {}
            data_reordered[dictionary['TIPO_DETECCION']
                           ][dictionary['DESCUBRIMIENTO']] = []
            data_reordered[dictionary['TIPO_DETECCION']
                           ][dictionary['DESCUBRIMIENTO']].append(dictionary['MASA'])
        else:
            if (not dictionary['DESCUBRIMIENTO'] in list(data_reordered[dictionary['TIPO_DETECCION']])):
                data_reordered[dictionary['TIPO_DETECCION']
                               ][dictionary['DESCUBRIMIENTO']] = []
                data_reordered[dictionary['TIPO_DETECCION']
                               ][int(dictionary['DESCUBRIMIENTO'])].append(dictionary['MASA'])
            else:
                data_reordered[dictionary['TIPO_DETECCION']
                               ][int(dictionary['DESCUBRIMIENTO'])].append(dictionary['MASA'])

    for data in data_reordered:
        data_reordered[data] = pd.Series(data_reordered[data])

    dataframe_dictionary = pd.DataFrame(data_reordered)

    for data in dataframe_dictionary:
        dataframe_dictionary[data] = dataframe_dictionary[data].apply(quit_nan)
        dataframe_dictionary[data] = dataframe_dictionary[data].apply(average)

    print(dataframe_dictionary)

    plt.plot(dataframe_dictionary)
    plt.title("Cantidad de planetas descubiertos según el tipo de detección")
    plt.xlabel("Año de descubrimiento")
    plt.ylabel("Masa promedio")
    plt.legend(list(data_reordered))

    plt.savefig('./assets/histogram-planet-mass-average.png')

    plt.show()

    pass


def masa_planetas_vs_masa_estrellas(datos: pd.DataFrame) -> None:
    """ Calcula y despliega un diagrama de dispersión donde en el eje x se
        encuentra la masa de los planetas y en el eje y se encuentra el logaritmo
        de la masa de las estrellas. Cada punto en el diagrama correspondera
        a un planeta y estara ubicado de acuerdo con su masa y la masa de la
        estrella más cercana.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    star_mass = datos["MASA_ESTRELLA"]

    planet_mass = datos["MASA"]

    star_mass = star_mass.apply(lambda x: np.log10(x))

    plt.scatter(planet_mass, star_mass)
    plt.title("Masa de los planetas vs. masa de la estrella más cercana")
    plt.xlabel("Masa del planeta")
    plt.ylabel("Masa de la estrella (log)")

    plt.savefig('./assets/scatter-mass-planet-star.png')

    plt.show()

    pass


def get_coords(ra: float, dec: float) -> tuple:
    row = int((99 - abs(sin(ra)*cos(dec)*100)))
    column = int(abs(cos(ra)*cos(dec)*100)+100)

    return (row, column)


def get_color_by_type(detection_type: str) -> tuple:
    if (detection_type == "Microlensing"):
        return (0.94, 0.10, 0.10)
    if (detection_type == "Radial Velocity"):
        return (0.1, 0.5, 0.94)
    if (detection_type == "Imaging"):
        return (0.34, 0.94, 0.1)
    if (detection_type == "Primary Transit"):
        return (0.10, 0.94, 0.85)
    if (detection_type == "Other"):
        return (0.94, 0.10, 0.85)
    if (detection_type == "Astrometry"):
        return (0.94, 0.65, 0.10)
    if (detection_type == "TTV"):
        return (1, 1, 1)


def graficar_cielo(datos: pd.DataFrame) -> list:
    """ Calcula y despliega una imagen donde aparece un pixel por cada planeta,
        usando colores diferentes que dependen del tipo de detección utilizado
        para descubirlo.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    Retorno:
        Una matriz de pixeles con la representacion del cielo
    """
    ROWS = 100
    COLUMNS = 200
    image = [0]*ROWS

    for row in range(0, ROWS):
        image[row] = [0]*COLUMNS

    for row in range(0, ROWS):
        for column in range(0, COLUMNS):
            image[row][column] = (0, 0, 0)

    data = datos[["TIPO_DETECCION", "RA", "DEC"]]

    for row in data.values.tolist():
        ra = row[1]
        dec = row[2]
        detection_type = row[0]
        row, column = get_coords(ra, dec)
        image[row][column] = get_color_by_type(detection_type)

    plt.figure(figsize=(9, 9))

    for i in range(0, ROWS):
        for j in range(0, COLUMNS):
            plt.plot(i, j, color=image[i][j])

    plt.savefig('./assets/graph-sky.png')

    plt.show()

    pass

    return image


def filtrar_imagen_cielo(imagen: list) -> None:
    """ Le aplica a la imagen un filtro de convolucion basado en la matriz
        [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]
    Parametros:
        imagen (list): una matriz con la imagen del cielo
    """
    pass
