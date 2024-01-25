import psycopg2
from Modelo.Sucursal import Sucursal
class DataBaseConection:
    def __init__(self): #constructor
        self.connection=None

    def StarConection(self):
        try:
            self.connection=psycopg2.connect(
                host='localhost',
                user='postgres',
                password='1234',
                database='BD_Centro_Comercial'
            )
            print('Conexion Exitosa...')
            cursor=self.connection.cursor()
            cursor.execute('Select version()')
            row=cursor.fetchone()
            print(row)
            return self.connection
        except Exception as ex:
            print('Error al conectarse a la base de datos: '+ex)
            return False

    def EndConection(self):
        if self.connection:
            self.connection.close()
            print('Conexion finalizada')

