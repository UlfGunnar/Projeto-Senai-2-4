from connection.connection import get_connection, get_connection_root

def criar_banco():
    conn = None
    cursor = None
    try:
        conn = get_connection_root()  # ← usa a sem banco
        cursor = conn.cursor()
        cursor.execute("""
            CREATE DATABASE IF NOT EXISTS db_dogtor
            DEFAULT CHARACTER SET utf8
            DEFAULT COLLATE utf8_general_ci
        """)
        print("✅ Banco criado!")
    except Exception as e:
        print("Erro ao criar banco:", e)
    finally:
        if cursor: cursor.close()
        if conn:   conn.close()

def criar_tabelas():
    try:
        conn = get_connection() 
        cursor = conn.cursor()

        # 1 — sem dependências
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cliente (
                cpf          CHAR(11)     NOT NULL PRIMARY KEY,
                nome_cliente VARCHAR(50)  NOT NULL,
                email        VARCHAR(80)  NOT NULL,
                celular      CHAR(11)     NOT NULL,
                bairro       VARCHAR(20),
                rua          CHAR(100),
                numero       CHAR(10),
                complemento  VARCHAR(50)
            ) DEFAULT CHARSET = utf8
        """)

        # 2 — sem dependências
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cargo (
                id_cargo   INT         AUTO_INCREMENT NOT NULL PRIMARY KEY,
                nome_cargo VARCHAR(20) NOT NULL
            ) DEFAULT CHARSET = utf8
        """)

        # 3 — sem dependências
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tipo_consulta (
                id_consulta INT          NOT NULL PRIMARY KEY,
                finalidade  VARCHAR(20),
                valor       DECIMAL(7,2)
            ) DEFAULT CHARSET = utf8
        """)

        # 4 — depende de cliente
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS animal (
                id_animal   INT         AUTO_INCREMENT PRIMARY KEY,
                fk_cpf      CHAR(11),
                nome_animal VARCHAR(30) NOT NULL,
                genero      CHAR(1)     NOT NULL,
                especie     VARCHAR(15) NOT NULL,
                raca        VARCHAR(15),
                peso        DECIMAL(5,2) NOT NULL,
                FOREIGN KEY (fk_cpf) REFERENCES cliente(cpf)
            ) DEFAULT CHARSET = utf8
        """)

        # 5 — depende de cargo
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS funcionarios (
                id_funcionario   INT         AUTO_INCREMENT NOT NULL PRIMARY KEY,
                fk_id_cargo      INT,
                nome_funcionario VARCHAR(60) NOT NULL,
                num_celular      CHAR(11)    NOT NULL,
                email            VARCHAR(80) NOT NULL,
                bairro           VARCHAR(20) NOT NULL,
                rua              CHAR(50)    NOT NULL,
                complemento      VARCHAR(50),
                dt_nascimento    DATE        NOT NULL,
                FOREIGN KEY (fk_id_cargo) REFERENCES cargo(id_cargo)
            ) DEFAULT CHARSET = utf8
        """)

        # 6 — depende de funcionarios, cliente, cargo
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS login (
                id_login       INT  AUTO_INCREMENT NOT NULL PRIMARY KEY,
                fk_funcionario INT,
                senha          TEXT NOT NULL,
                fk_cpf         CHAR(11),
                fk_cargo       INT,
                FOREIGN KEY (fk_funcionario) REFERENCES funcionarios(id_funcionario),
                FOREIGN KEY (fk_cpf)         REFERENCES cliente(cpf),
                FOREIGN KEY (fk_cargo)       REFERENCES cargo(id_cargo)
            ) DEFAULT CHARSET = utf8
        """)

        # 7 — depende de funcionarios, animal, cliente, tipo_consulta
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS consulta (
                id_consulta      INT         AUTO_INCREMENT NOT NULL PRIMARY KEY,
                fk_funcionario   INT,
                fk_animal        INT         NOT NULL,
                fk_cpf           CHAR(11),
                fk_tipo_consulta INT         NOT NULL,
                dt_consulta      DATE        NOT NULL,
                hr_consulta      TIME        NOT NULL,
                status           VARCHAR(15) DEFAULT 'EM ANDAMENTO',
                FOREIGN KEY (fk_funcionario)   REFERENCES funcionarios(id_funcionario),
                FOREIGN KEY (fk_animal)        REFERENCES animal(id_animal),
                FOREIGN KEY (fk_cpf)           REFERENCES cliente(cpf),
                FOREIGN KEY (fk_tipo_consulta) REFERENCES tipo_consulta(id_consulta)
            ) DEFAULT CHARSET = utf8
        """)

        # 8 — depende de animal, tipo_consulta, cliente, consulta
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS historico (
                id_historico INT         AUTO_INCREMENT NOT NULL PRIMARY KEY,
                fk_animal    INT         NOT NULL,
                fk_tipo      INT         NOT NULL,
                fk_cpf       CHAR(11)    NOT NULL,
                fk_consulta  INT         NOT NULL,
                remedio      VARCHAR(40) NOT NULL,
                diagnostico  VARCHAR(40) NOT NULL,
                FOREIGN KEY (fk_animal)  REFERENCES animal(id_animal),
                FOREIGN KEY (fk_tipo)    REFERENCES tipo_consulta(id_consulta),
                FOREIGN KEY (fk_cpf)     REFERENCES cliente(cpf),
                FOREIGN KEY (fk_consulta) REFERENCES consulta(id_consulta)
            ) DEFAULT CHARSET = utf8
        """)

        conn.commit()
        print("✅ Tabelas criadas com sucesso!")

    except Exception as e:
        print("Erro ao criar tabelas:", e)
    finally:
        if cursor: cursor.close()  
        if conn:   conn.close()  


