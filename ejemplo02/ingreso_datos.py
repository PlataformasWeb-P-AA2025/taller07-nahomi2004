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
# Y crear un array para luego relacionarlo con un jugador
lista_club = [] 

for index, row in clubs_csv.iterrows():
    club = Club(
        nombre=row[0],
        deporte=row[1],
        fundacion=int(row[2])  # Aseguramos que sea entero
    )
    lista_club.append(club)
    session.add(club)

# Reviso si se han guardado correctamente los club en la lista
# print(lista_club)

# Hago lo mismo para jugadores
# Leo el csv de jugadores
jugadores_csv = pd.read_csv("data/datos_jugadores.txt", delimiter=';', header=None)

# Bueno, no es lo mismo literalmente
# Lo primero que hago es comprobar la primera celda del txt
# de jugadores (esta contiene el nombre del equipo), es
# igual a algun nombre de la lista de objetos lista_club
# Si es asi, creo el objeto jugador y le envio de una vez
# el objeto club, para que se de la relacion.
# Se puede hacer de una forma mas efectiva? Si, pero
# me gusta la que acabo de hacer porque la entiendo jeje.
for index, row in jugadores_csv.iterrows():
    if row[0] == lista_club[0].nombre:
        jugador = Jugador(
            nombre=row[3],
            dorsal=row[2], 
            # Le cambie el dorsal de Layan Loer porque como no habia ; o dato, lo tomaba a el como dorsal xd
            posicion=row[1],
            club=lista_club[0]
        )
    

    if row[0] == lista_club[1].nombre: 
        jugador = Jugador(
            nombre=row[3],
            dorsal=row[2],
            posicion=row[1],
            club=lista_club[1]
        )
    

    if row[0] == lista_club[2].nombre:
        jugador = Jugador(
            nombre=row[3],
            dorsal=row[2],
            posicion=row[1],
            club=lista_club[2]
        )
    

    if row[0] == lista_club[3].nombre:
        jugador = Jugador(
            nombre=row[3],
            dorsal=row[2],
            posicion=row[1],
            club=lista_club[3]
        )
    

    session.add(jugador)
    

# se confirma las transacciones
session.commit()
