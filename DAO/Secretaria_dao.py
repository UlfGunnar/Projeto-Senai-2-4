from connection.connection import get_connection

class SecretariaDAO:
    def inserir_secretaria(self, secretaria):
        try:    
            conn = get_connection()
            cursor = conn.cursor()

            sql = """
            INSERT INTO secretaria (
                matricula_secretaria, nome_secretaria, rua, complemento, dt_nascimento, email, num_celular
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            valores = (
                secretaria.matricula_secretaria,
                secretaria.nome_secretaria,
                secretaria.rua,
                secretaria.complemento,
                secretaria.dt_nascimento,
                secretaria.email,
                secretaria.num_celular
            )

            cursor.execute(sql, valores)
            conn.commit()

        except Exception as e:
            print("Erro ao inserir secretaria: ", e)

        finally:
            cursor.close()
            conn.close()