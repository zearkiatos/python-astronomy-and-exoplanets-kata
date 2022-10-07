from dis import disco
from turtle import title
import pandas as pd
import matplotlib.pyplot as plt
import math as m
import numpy as np

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


def cantidad_y_tipo_deteccion(datos: pd.DataFrame) -> None:
    """ Calcula y despliega un diagrama de lineas donde aparece una linea por
        cada tipo de deteccion y se muestra la cantidad de planetas descubiertos
        en cada anho, para ese tipo de deteccion.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    pass


def masa_promedio_y_tipo_deteccion(datos: pd.DataFrame) -> None:
    """ Calcula y despliega un diagrama de lineas donde aparece una linea por
        cada tipo de detección y se muestra la masa promedio de los planetas descubiertos
        en cada anho, para ese tipo de deteccion.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
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
    pass


def graficar_cielo(datos: pd.DataFrame) -> list:
    """ Calcula y despliega una imagen donde aparece un pixel por cada planeta,
        usando colores diferentes que dependen del tipo de detección utilizado
        para descubirlo.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    Retorno:
        Una matriz de pixeles con la representacion del cielo
    """
    pass


def filtrar_imagen_cielo(imagen: list) -> None:
    """ Le aplica a la imagen un filtro de convolucion basado en la matriz
        [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]
    Parametros:
        imagen (list): una matriz con la imagen del cielo
    """
    pass
