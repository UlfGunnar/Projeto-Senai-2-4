from connection.connection import get_connection

class LoginDAO:
    def inserir_login(self, login):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            sql = """
            INSERT INTO login( 
                fk_funcionario, senha, fk_cpf, fk_cargo
            ) VALUES (%s, %s, %s, %s)
            """

            valores = (
                  login.fk_funcionario,
                  login.senha,
                  login.fk_cpf,
                  login.fk_cargo
            )

            cursor.execute(sql, valores)
            conn.commit()

        except Exception as e:
            print("Erro ao inserir login: ", e)

        finally:
            cursor.close()
            conn.close()
