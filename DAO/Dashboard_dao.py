from connection.connection import get_connection

class Tipos_de_consulta():
    def listar_consultas(self):
        conn = None
        cursor = None

        try:
            conn = get_connection()

            if conn is None:
                print("Erro na conexão")
                return[]
            
            cursor = conn.cursor()
            sql = """
            SELECT
                tb1.finalidade,
                COUNT(tb2.id_consulta) as total_consultas
            FROM db_dogtor.tipo_consulta tb1
                left join consulta tb2 on tb1.id_consulta = tb2.fk_id_consulta
                group by tb1.id_consulta, tb1.finalidade;
            """

            cursor.execute(sql)

            resultados = cursor.fetchall()

            return resultados
        
        except Exception as e:
            print("Erro ao listar soma de consultas", e)
            return[]

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
