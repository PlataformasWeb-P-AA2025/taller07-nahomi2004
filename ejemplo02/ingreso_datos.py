from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
import pandas as pd

# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Accedo al txt usando pandas
# Especifico que no tiene encabezados para que la primera linea
# no sea tomada como encabezado
clubs_csv = pd.read_csv("data/datos_clubs.txt", delimiter=';', header=None)

# Reviso si esta tomando bien los datos
# print(clubs_csv)
# Ahora los encabezados son 0, 1 y 2
# 0 es el nombre, 1 el deporte, 2 el anio de fundacion
# print(clubs_csv[0])
# print(clubs_csv[0][0])

# Guardo a los clubs
# Recorrer cada fila del DataFrame y crear objetos Club
for index, row in clubs_csv.iterrows():
    club = Club(
        nombre=row[0],
        deporte=row[1],
        fundacion=int(row[2])  # Aseguramos que sea entero
    )
    session.add(club)

# Hago lo mismo para jugadores
jugadores_csv = pd.read_csv("data/datos_jugadores.txt", delimiter=';', header=None)

for index, row in jugadores_csv.iterrows():
    jugador = Jugador(
        nombre=row[0],
        dorsal=row[1],
        posicion=int(row[2])  # Aseguramos que sea entero
    )
    session.add(jugador)

# se confirma las transacciones
session.commit()
