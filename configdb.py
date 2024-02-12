

import pyodbc 
import os
from dotenv import load_dotenv
import json

load_dotenv()

class ConfigDataBase():

    def __init__(self, table):
        self.table = table

    def run(self):
        try:
            driver = os.environ.get('DRIVER')
            pwd = os.environ.get('PWD')
            conn = pyodbc.connect(
                f'DRIVER={driver};SERVER=localhost;PORT=1433;UID=sa;PWD={pwd}', 
                autocommit=True
            )
            cursor = conn.cursor()
        except Exception  as e:
            print(f"Error: {e}")

        try:
                        
            cursor.execute(f"""SELECT Name FROM sys.Databases;""")
            print("Sys Databases Inicial")
            for row in cursor.fetchall():
                print(row)

            cursor.execute(f"""RESTORE FILELISTONLY FROM DISK = N'Testing_ETL.bak';""")
            cursor.execute(f"""RESTORE DATABASE mydb FROM DISK = N'Testing_ETL.bak' WITH REPLACE, MOVE 'Testing_ETL' TO '/var/opt/mssql/data/Testing_ETL.mdf', MOVE 'Testing_ETL_log' TO '/var/opt/mssql/data/Testing_ETL_log.ldf';""")

            while cursor.nextset():
                pass 
            cursor.close()
            
            cursor = conn.cursor()
            cursor.execute(f"""SELECT Name FROM sys.Databases;""")
            print("Sys Databases Final")
            for row in cursor.fetchall():
                print(row)

        except Exception  as e:
            print(f"Error: {e}")

        cursor.commit()
        cursor.close()


if __name__ == "__main__":
    table = "Unificado"
    objeto = ConfigDataBase(table)
    objeto.run()
    
    
    


    
