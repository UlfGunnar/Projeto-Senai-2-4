from connection.connection import get_connection

class FuncionarioDAO:
    def inserir_funcionario(self, funcionario):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            sql = """
            INSERT INTO funcionarios(
            fk_id_cargo, nome_funcionario, num_celular, email, bairro, rua, complemento, dt_nascimento
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """

            valores = (
                funcionario.fk_id_cargo,
                funcionario.nome_funcionario,
                funcionario.num_celular,
                funcionario.email,
                funcionario.bairro,
                funcionario.rua,
                funcionario.complemento,
                funcionario.dt_nascimento
            )

            cursor.execute(sql, valores)
            conn.commit()
            return cursor.lastrowid

        except Exception as e:
            print("Erro ao inserir funcionario", e)

        finally:
            cursor.close()
            conn.close()

    def inserir_login(self, login):
        try:    
            conn = get_connection()
            cursor = conn.cursor()

            sql = """
            INSERT INTO login (
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
            print("Erro ao inserir Cliente: ", e)
            
        finally:
            cursor.close()
            conn.close()