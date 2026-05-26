from connection.connection import get_connection

class ClienteDAO:
    def inserir_cliente(self, cliente):
        conn = get_connection()
        
        if conn is None:
            print("Erro na conexão com o banco de dados.")
            return
        
        cursor = conn.cursor()

        sql = """
        INSERT INTO cliente (
            cpf, nome, email, bairro, rua, numero, complemento, celular
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        valores = (
            cliente.cpf,
            cliente.nome,
            cliente.email,
            cliente.bairro,
            cliente.rua,
            cliente.numero,
            cliente.complemento,
            cliente.celular
        )

        cursor.execute(sql, valores)
        conn.commit()

        cursor.close()
        conn.close()