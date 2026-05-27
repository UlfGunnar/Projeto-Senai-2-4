from connection.connection import get_connection 

class AnimalDAO:
    def inserir_animal(self, animal):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            sql = """
            INSERT INTO animal (
                id_animal, cpf, nome, raca, especie, genero, peso
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            valores = (
                animal.id_animal,
                animal.cpf,
                animal.nome,
                animal.raca,
                animal.especie,
                animal.genero,
                animal.peso
            )

            cursor.execute(sql, valores)
            conn.commit()
        
        except Exception as e:
            print("Erro ao inserir animal: ", e)

        finally:
            cursor.close()
            conn.close()        