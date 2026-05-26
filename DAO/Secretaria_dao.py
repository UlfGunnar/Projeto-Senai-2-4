from connection.connection import get_connection

class SecretariaDAO:
    def inserir_secretaria(self, secretaria):
        conn = get_connection()
        
        if conn is None:
            print("Erro na conexão com o banco de dados.")
            return
        
        cursor = conn.cursor()

        sql = """
        INSERT INTO secretaria (
            matricula_secretaria, nome, rua, complemento, data_nascimento, email, celular
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        valores = (
            secretaria.matricula_secretaria,
            secretaria.nome,
            secretaria.rua,
            secretaria.complemento,
            secretaria.data_nascimento,
            secretaria.email,
            secretaria.celular
        )

        cursor.execute(sql, valores)
        conn.commit()

        cursor.close()
        conn.close()