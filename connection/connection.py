import mysql.connector

def get_connection():
    try:
        return mysql.connector.connect(
            host='localhost',
            user='root',        
            password='dogtor2026',
            database='db_dogtor',
            port=3306
        )
    except mysql.connector.Error as err:
        print(f"Erro ao connectar ao MySQL: {err}")
        return None