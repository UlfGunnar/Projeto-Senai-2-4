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

    def mostrar_historico_cliente(self, cpf_usuario):
        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True) #vai retornar em dicionario automáticamente 
            sql = """
                select 
                    a.nome_animal								as nome_animal,
                    a.especie									as espcie,
                    CONCAT(c.dt_consulta, ' ', c.hr_consulta)   as data_hora,
                    c.status                                    as status,
                    tc.valor 									as valor,
                    tc.finalidade								as finalidade
                from animal as a
                inner join consulta as c on a.id_animal = c.fk_animal
                inner join tipo_consulta as tc on tc.id_consulta = c.id_consulta
                WHERE c.fk_cpf = %s and c.status = 'CONCLUIDO'
            """
        
            cursor.execute(sql, (cpf_usuario,))

            return cursor.fetchall()
        
        except Exception as e:
            print("Erro ao inserir funcionario", e)

        finally:
            cursor.close()
            conn.close()

    def mostrar_historico_funcionario(self):  # sem cpf_usuario se não usa
        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = """
                SELECT 
                    a.nome_animal                               AS nome_animal,
                    a.especie                                   AS especie,
                    CONCAT(c.dt_consulta, ' ', c.hr_consulta)  AS data_hora,
                    c.status                                    AS status,
                    tc.valor                                    AS valor,
                    tc.finalidade                               AS finalidade
                FROM animal AS a
                INNER JOIN consulta AS c         ON a.id_animal   = c.fk_animal
                INNER JOIN tipo_consulta AS tc   ON tc.id_consulta = c.fk_tipo_consulta
                WHERE c.status = 'CONCLUIDO'
            """
            cursor.execute(sql)
            return cursor.fetchall()

        except Exception as e:
            print("Erro ao buscar histórico funcionario:", e)
            return []

        finally:
            cursor.close()
            conn.close()