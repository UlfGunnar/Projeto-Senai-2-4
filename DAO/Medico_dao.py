from connection.connection import get_connection

class MedicoDAO:
    def inserir_medico(self, medico):
        try:    
            conn = get_connection()
            cursor = conn.cursor()

            sql = """
            INSERT INTO medico(
                matricula_medico, nome, rua, complemento, data_nascimento, email, celular
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """

            valores = (
                medico.matricula_medico,
                medico.nome,
                medico.rua,
                medico.complemento,
                medico.data_nascimento,
                medico.email,
                medico.celular
            )

            cursor.execute(sql, valores)
            conn.commit()

        except Exception as e:
            print("Erro ao inserir medico: ", e)
        
        finally:
            cursor.close()
            conn.close()
        
        