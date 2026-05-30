from connection.connection import get_connection

class HistoricoDAO:
    def inserir_historico(self, historico):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            sql = """
            INSERT INTO historico(
                fk_animal, fk_tipo, fk_cpf, fk_consulta, remedio, diagnostico
            ) VALUES (%s, %s, %s, %s, %s, %s)
            """

            valores = (
                historico.fk_animal,
                historico.fk_tipo,
                historico.fk_cpf,
                historico.fk_consulta,
                historico.remedio,
                historico.diagnostico,
            )

            cursor.execute(sql, valores)
            conn.commit()

        except Exception as e:
            print("Erro ao inserir historico: ", e)

        finally:
            cursor.close()
            conn.close()