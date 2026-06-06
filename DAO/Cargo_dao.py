from connection.connection import get_connection

class CargoDAO:
    def inserir_cargo(self, cargo):
        try:
            conn = get_connection() 
            cursor = conn.cursor()
            sql = """
            INSERT INTO cargo (
                nome_cargo
            ) VALUES (%s)
            """

            valores = (
                cargo.nome_cargo,
            )

            cursor.execute(sql, valores)
            conn.commit()

        except Exception as e:
            print("Erro ao inserir cargo: ", e)
            
        finally:
            cursor.close()
            conn.close()