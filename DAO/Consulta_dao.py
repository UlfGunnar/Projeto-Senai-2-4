from connection.connection import get_connection

class ConsultaDAO:
    def inserir_consulta(self, consulta):
        try:
            conn = get_connection() 
            cursor = conn.cursor()

            sql = """
            INSERT INTO consulta (
                id_consulta, fk_matricula_medico, fk_animal, fk_cpf, fk_tipo_consulta, dt_consulta, hr_consulta
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            valores = (
                consulta.id_consulta,
                consulta.fk_matricula_medico,
                consulta.fk_animal,
                consulta.fk_cpf,
                consulta.fk_tipo_consulta,
                consulta.dt_consulta,
                consulta.hr_consulta
            )

            cursor.execute(sql, valores)
            conn.commit()

        except Exception as e:
            print("Erro ao inserir consulta: ", e)
            
        finally:
            cursor.close()
            conn.close()