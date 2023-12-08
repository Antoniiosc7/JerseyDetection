
import pandas as pd
import matplotlib.pyplot as plt


def compruebaDB(string):
    db = pd.read_csv("male_players.csv", dtype=str)
    selected_columns = ["short_name", "long_name", "club_jersey_number", "nation_jersey_number", "club_name"]
    selected_data = db[selected_columns].copy()
    seleccionada = db["short_name"].values.tolist()
    listaApellidos = [max(name.split(), key=len) for name in seleccionada]
    selected_data.loc[:, "apellidos"] = listaApellidos

    if(len(string)>0):
        dorsal = (string[1])
        resultado = encontrar_jugadores(string[0], listaApellidos)
    else:
        dorsal = string
        resultado = encontrar_jugadores(string, listaApellidos)
        
    if len(resultado) > 1 and dorsal and any(str(d).isdigit() for d in dorsal):
        res=buscar_por_dorsal(selected_data, dorsal, resultado)
        imprimir_jugadores_y_equipos_sin_repetir(res, selected_data)
    else:
        print(int(str(dorsal)))
        imprimir_jugadores_y_equipos_sin_repetir(resultado, selected_data)
        
def imprimir_jugadores_y_equipos_sin_repetir(filas, dataframe):
    long_names = dataframe.loc[filas, "long_name"].tolist()
    long_names_sin_repetir = list(set(long_names))

    for long_name in long_names_sin_repetir:
        fila = dataframe[dataframe["long_name"] == long_name].iloc[0]
        equipo = fila["club_name"]
        dorsalEquipo = fila["club_jersey_number"]
        print(f"Jugador detectado: {long_name}, lleva el número {dorsalEquipo} en el equipo: {equipo}")

def buscar_por_dorsal(db, dorsal, filas_a_comprobar):
    return [i for i, fila in enumerate(db.itertuples()) if i in filas_a_comprobar and (lambda x: x if x is None else int(x))(getattr(fila, "club_jersey_number")) == int(dorsal)]

def encontrar_jugadores(cadena, listaJugadores):
    cadena_minusculas = (str(cadena)).lower()
    posiciones = [i for i, jugador in enumerate(listaJugadores) if jugador.lower() in cadena_minusculas]
    return posiciones