from connection.connection import get_connection

class SecretariaDAO:
    def inserir_secretaria(self, secretaria):
        try:    
            conn = get_connection()
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

        except Exception as e:
            print("Erro ao inserir secretaria: ", e)

        finally:
            cursor.close()
            conn.close()