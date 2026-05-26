from connection.connection import get_connection 

class AnimalDAO:
    def inserir_animal(self, animal):
        conn = get_connection()
        
        if conn is None:
            print("Erro na conexão com o banco de dados.")
            return
        
        cursor = conn.cursor()

        sql = """
        INSERT INTO animal (
            nome, cpf, raca, especie, genero, peso
        ) VALUES (%s, %s, %s, %s, %s, %s,)
        """

        valores = (
            animal.nome,
            animal.cpf,
            animal.raca,
            animal.especie,
            animal.genero,
            animal.peso
        )

        cursor.execute(sql, valores)
        conn.commit()

        cursor.close()
        conn.close()        