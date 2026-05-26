from connection.connection import get_connection

class HistoricoDAO:
    def inserir_historico(sel, historico):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            sql = """
            INSERT INTO historico(
                id_historico, id_animal, id_tipo, cpf, id_consulta, remedio, diagnostico, data_consulta, hora_consulta
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            valores = (
                historico.id_historico,
                historico.id_animal,
                historico.id_tipo,
                historico.cpf,
                historico.id_consulta,
                historico.remedio,
                historico.diagnostico,
                historico.data_consulta,
                historico.hora_consulta
            )

            cursor.execute(sql, valores)
            conn.commit()

        except Exception as e:
            print("Erro ao inserir historico: ", e)

        finally:
            cursor.close()
            conn.close()