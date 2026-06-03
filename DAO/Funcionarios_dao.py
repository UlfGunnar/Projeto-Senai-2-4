from connection.connection import get_connection

class FuncionarioDAO:
    def inserir_funcionario(self, funcionario):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            sql = """
            INSERT INTO funcionarios(
            nome_funcionario, num_celular, email, bairro, rua, complemento, dt_nascimento
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            valores = (
                consulta.nome_funcionario,
                consulta.num_celular,
                consulta.email,
                consulta.bairro,
                consulta.rua,
                consulta.complemento,
                consulta.dt_nascimento
            )

            cursor.execute(sql, valores)
            conn.commit()

        except Exception as e:
            print("Erro ao inserir funcionario", e)

        finally:
            cursor.cluse()
            conn.close()