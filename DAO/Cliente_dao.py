from connection.connection import get_connection

class ClienteDAO:
    def inserir_cliente(self, cliente):
        try:    
            conn = get_connection()
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

        except Exception as e:
            print("Erro ao inserir Cliente: ", e)
            
        finally:
            cursor.close()
            conn.close()