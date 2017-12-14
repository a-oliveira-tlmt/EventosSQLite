import sqlite3
from model.Evento import Evento
from database.config import database
from datetime import date

def listarEventos():
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        # lendo os dados
        cursor.execute("""
          SELECT * FROM evento;
        """)

        eventos = []

        for linha in cursor.fetchall():
            nome = linha[1]
            dataInicioStr = linha[2]
            dataInicioObj = str2Time(dataInicioStr)
            dataFimStr = linha[3]
            dataFimObj = str2Time(dataFimStr)
            evento = Evento(nome, dataInicioObj, dataFimObj)
            eventos.append(evento)

        conn.close()
    except sqlite3.Error:
        print("Problema com o banco de dados")

    return eventos
    
def str2Time(dataStr):
	strData = dataStr.split(' ')
	strDataSep = strData.split('-')
	DataObj = date( int(strDataSep[0]), int(strDataSep[1]), int(strDataSep[2]) )
	return DataObj

def main(arg = []):
    eventos = listarEventos()

    for evento in eventos:
        print(evento)

if (__name__ == "__main__"):
    main()
