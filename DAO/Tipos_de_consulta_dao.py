from connection.connection import get_connection

class TiposDeConsultaDAO:
    def inserir_tipo_consulta(self, tipo_consulta):
        
        try:
            conn = get_connection()  
            cursor = conn.cursor()

            sql = """
            INSERT INTO tipo_consulta (
                id_consulta, finalidade, valor
            ) VALUES (%s, %s, %s)
            """

            valores = (
                tipo_consulta.id_consulta,
                tipo_consulta.finalidade,
                tipo_consulta.valor
            )

            cursor.execute(sql, valores)
            conn.commit()

        except Exception as e:
            print("Erro ao inserir Tipo de consulta: ", e)

        finally:
            cursor.close()
            conn.close()    