from connection.connection import get_connection

class ConsultaDAO:
    def inserir_consulta(self, consulta):
        conn = get_connection()
        
        if conn is None:
            print("Erro na conexão com o banco de dados.")
            return
        
        cursor = conn.cursor()

        sql = """
        INSERT INTO consulta (
            id_consulta, matricula_medico, id_animal, cpf, tipo _consulta, data, hora
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        valores = (
            consulta.id_consulta,
            consulta.matricula_medico,
            consulta.id_animal,
            consulta.cpf,
            consulta.tipo_consulta,
            consulta.data,
            consulta.hora
        )

        cursor.execute(sql, valores)
        conn.commit()

        cursor.close()
        conn.close()