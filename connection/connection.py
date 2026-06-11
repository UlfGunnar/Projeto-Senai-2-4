import mysql.connector

# ← conexão SEM banco — só para criar o db_dogtor
def get_connection_root():
    try:
        conn = mysql.connector.connect(
            host     = "localhost",
            user     = "root",
            password = "",
            port     = 3306
            # ← sem database aqui
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao MySQL: {err}")
        return None

# ← conexão COM banco — usada em todo o resto do projeto
def get_connection():
    try:
        conn = mysql.connector.connect(
            host     = "localhost",
            user     = "root",
            password = "",
            database = "db_dogtor",
            port     = 3306
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao MySQL: {err}")
        return None
