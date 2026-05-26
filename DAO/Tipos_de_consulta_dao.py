from connection.connection import get_connection

class TiposDeConsultaDAO:
    def inserir_tipo_consulta(self, tipo_consulta):
        conn = get_connection()
        
        if conn is None:
            print("Erro na conexão com o banco de dados.")
            return
        
        cursor = conn.cursor()

        sql = """
        INSERT INTO tipo_consulta (
            id_consulta, tipo, valor
        ) VALUES (%s, %s, %s)
        """

        valores = (
            tipo_consulta.id_consulta,
            tipo_consulta.tipo,
            tipo_consulta.valor
        )

        cursor.execute(sql, valores)
        conn.commit()

        cursor.close()
        conn.close()    