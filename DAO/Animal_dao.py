from connection.connection import get_connection 

class AnimalDAO:
    def inserir_animal(self, animal):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            sql = """
            INSERT INTO animal (
                fk_cpf, nome_animal, raca, especie, genero, peso
            ) VALUES (%s, %s, %s, %s, %s, %s)
            """

            valores = (
                animal.fk_cpf,
                animal.nome_animal,
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