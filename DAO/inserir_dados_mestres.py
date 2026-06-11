from connection.connection import get_connection

def inserir_dados_mestre():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # tipo_consulta
        cursor.execute("""
            INSERT IGNORE INTO tipo_consulta (id_consulta, finalidade, valor) VALUES
            (1, 'Check-up',             149.99),
            (2, 'Consulta Pediatrica',  100.00),
            (3, 'Consulta Geriatrica',  169.99)
        """)

        # cargo
        cursor.execute("""
            INSERT IGNORE INTO cargo (id_cargo, nome_cargo) VALUES
            (1, 'Veterinario'),
            (2, 'Secretaria')
        """)

        conn.commit()
        print("✅ Dados mestre inseridos!")

    except Exception as e:
        print("Erro ao inserir dados mestre:", e)
    finally:
        if cursor: cursor.close()
        if conn:   conn.close()