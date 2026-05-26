from connection.connection import get_connection

class MedicoDAO:
    def inserir_medico(self, medico):
        conn = get_connection()
        
        if conn is None:
            print("Erro na conexão com o banco de dados.")
            return
        
        cursor = conn.cursor()

        sql = """
        INSERT INTO medico(
            matricula_medico, nome, rua, numero, complemento, data_nascimento, email
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        valores = (
            medico.matricula_medico,
            medico.nome,
            medico.rua,
            medico.numero,
            medico.complemento,
            medico.data_nascimento,
            medico.email
        )

        cursor.execute(sql, valores)
        conn.commit()

        cursor.close()
        conn.close()