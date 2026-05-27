from connection.connection import get_connection

class LoginDAO:
    def inserir_login(self, login):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            sql = """
            INSERT INTO login( 
                id_conta, fk_cpf, fk_matricula_secretaria, fk_matricula_medico, usuario, senha
            ) VALUES (%s, %s, %s, %s, %s, %s,)
            """

            valores = (
                  login.id_conta,
                  login.fk_cpf,
                  login.fk_matricula_secretaria,
                  login.fk_matricula_medico,
                  login.usuario,
                  login.senha
            )

            cursor.execute(sql, valores)
            conn.commit()

        except Exception as e:
            print("Erro ao inserir login: ", e)

        finally:
            cursor.close()
            conn.close()
