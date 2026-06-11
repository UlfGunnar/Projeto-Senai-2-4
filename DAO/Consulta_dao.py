from connection.connection import get_connection

class ConsultaDAO:
    def inserir_consulta(self, consulta):
        try:
            conn = get_connection() 
            cursor = conn.cursor()
            sql = """
            INSERT INTO consulta (
                fk_funcionario, fk_animal, fk_cpf, fk_tipo_consulta, dt_consulta, hr_consulta
            ) VALUES (%s, %s, %s, %s, %s, %s)
            """

            valores = (
                consulta.fk_funcionario,
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

    def acompanhar_consulta(self, cpf_usuario):
        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True) #vai retornar em dicionario automáticamente 
            sql = """
                SELECT
                    tb1.nome_animal                                 as nome_animal,
                    tb1.especie                                     as especie,
                    CONCAT(tb2.dt_consulta, ' ', tb2.hr_consulta)   as data_hora,
                    tb2.status                                      as status,
                    tb3.finalidade                                  as finalidade
                FROM db_dogtor.animal tb1
                inner join consulta tb2 on tb2.fk_animal = tb1.id_animal
                inner join tipo_consulta tb3 on tb3.id_consulta = tb2.id_consulta
                WHERE tb2.fk_cpf = %s;
            """
        
            cursor.execute(sql, (cpf_usuario,))

            return cursor.fetchall()
        
        except Exception as e:
            print("Erro ao inserir funcionario", e)

        finally:
            cursor.close()
            conn.close()

    def buscar_consultas_gerenciar(self):
        conn = None
        cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = """
                SELECT
                    c.id_consulta                           AS id,
                    a.nome_animal                           AS nome_pet,
                    cli.nome_cliente                        AS tutor,
                    tc.finalidade                           AS tipo_consulta,
                    DATE_FORMAT(c.dt_consulta, '%d/%m/%Y')  AS data_consulta
                FROM consulta AS c
                INNER JOIN animal AS a         ON a.id_animal    = c.fk_animal
                INNER JOIN cliente AS cli      ON cli.cpf        = c.fk_cpf
                INNER JOIN tipo_consulta AS tc ON tc.id_consulta = c.fk_tipo_consulta
                ORDER BY c.id_consulta ASC
            """
            cursor.execute(sql)
            return cursor.fetchall()

        except Exception as e:
            print("Erro ao buscar consultas:", e)
        finally:
            if cursor: cursor.close()
            if conn:   conn.close()

    def buscar_totais_dashboard(self):
        conn = None
        cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = """
                SELECT
                    tc.finalidade        AS tipo,
                    COUNT(c.id_consulta) AS total
                FROM consulta AS c
                INNER JOIN tipo_consulta AS tc ON tc.id_consulta = c.fk_tipo_consulta
                GROUP BY tc.finalidade
            """
            cursor.execute(sql)
            return cursor.fetchall()

        except Exception as e:
            print("Erro ao buscar totais:", e)
        finally:
            if cursor: cursor.close()
            if conn:   conn.close()