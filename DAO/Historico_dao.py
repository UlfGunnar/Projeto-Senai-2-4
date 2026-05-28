from connection.connection import get_connection

class HistoricoDAO:
    def inserir_historico(self, historico):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            sql = """
            INSERT INTO historico(
                fk_animal, fk_tipo, fk_cpf, fk_consulta, remedio, diagnostico, fk_data, fk_hora
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """

            valores = (
                historico.fk_animal,
                historico.fk_tipo,
                historico.fk_cpf,
                historico.fk_consulta,
                historico.remedio,
                historico.diagnostico,
                historico.fk_data,
                historico.fk_hora
            )

            cursor.execute(sql, valores)
            conn.commit()

        except Exception as e:
            print("Erro ao inserir historico: ", e)

        finally:
            cursor.close()
            conn.close()