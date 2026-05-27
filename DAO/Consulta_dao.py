from connection.connection import get_connection

class ConsultaDAO:
    def inserir_consulta(self, consulta):
        try:
            conn = get_connection() 
            cursor = conn.cursor()

            sql = """
            INSERT INTO consulta (
                id_consulta, matricula_medico, id_animal, cpf, tipo_consulta, data, hora, residencial
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """

            valores = (
                consulta.id_consulta,
                consulta.matricula_medico,
                consulta.id_animal,
                consulta.cpf,
                consulta.tipo_consulta,
                consulta.data,
                consulta.hora,
                consulta.residencial
            )

            cursor.execute(sql, valores)
            conn.commit()

        except Exception as e:
            print("Erro ao inserir consulta: ", e)
            
        finally:
            cursor.close()
            conn.close()