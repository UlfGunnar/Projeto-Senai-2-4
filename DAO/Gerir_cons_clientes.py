from connection.connection import get_connection

class ConsultaDAO():

    def listar_consultas_cliente(self): 
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
                tb1.nome_animal,
                tb1.especie,
                tb2.dt_consulta,
                tb2.hr_consulta,
                tb2.status,
                tb3.finalidade
            FROM animal tb1
            INNER JOIN consulta tb2 
                ON tb1.id_animal = tb2.fk_animal
            INNER JOIN tipo_consulta tb3 
                ON tb2.fk_tipo_consulta = tb3.id_tipo
            WHERE tb2.fk_cpf = %s;
                """

            cursor.execute(sql)

            resultados = cursor.fetchall()

            return resultados
        
        except Exception as e:
            print("Erro ao listar consultas", e)
            return[]

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()



