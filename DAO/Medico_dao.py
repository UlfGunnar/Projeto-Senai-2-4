from connection.connection import get_connection

class MedicoDAO:
    def inserir_medico(self, medico):
        try:    
            conn = get_connection()
            cursor = conn.cursor()

            sql = """
            INSERT INTO medico(
                matricula_medico, nome_medico, bairro, rua, complemento, dt_nascimento, email, num_celular
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """

            valores = (
                medico.matricula_medico,
                medico.nome_medico,
                medico.dt_nascimento,
                medico.num_celular,
                medico.email,
                medico.bairro,
                medico.rua,
                medico.complemento
            )

            cursor.execute(sql, valores)
            conn.commit()

        except Exception as e:
            print("Erro ao inserir medico: ", e)
        
        finally:
            cursor.close()
            conn.close()
        
        