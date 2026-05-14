CREATE DATABASE IF NOT EXISTS db_dogtor
default character set utf8
default collate utf8_general_ci;

CREATE TABLE IF NOT EXISTS cliente (
    
    id_cpf CHAR(11) NOT NULL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(80)NOT NULL,
    num_celular CHAR(11),
    bairro VARCHAR(20) NOT NULL,
    rua CHAR(50) NOT NULL,
	num_residencia CHAR(10) NOT NULL,
    complemento VARCHAR(50)
)
default charset = utf8;

CREATE TABLE IF NOT EXISTS animal (  

	id_animal INT AUTO_INCREMENT PRIMARY KEY,
    fk_cpf CHAR(11) NOT NULL,
    nome_animal VARCHAR(30) NOT NULL,
    genero_animal CHAR(1) NOT NULL,
    especie VARCHAR(15) NOT NULL,
    raca VARCHAR(15),
	peso_animal DECIMAL(5,2) NOT NULL,
    
    FOREIGN KEY (fk_cpf) REFERENCES cliente(id_cpf)   
) 
default charset = utf8;

CREATE TABLE IF NOT EXISTS medico ( 
	
    matricula_medico INT AUTO_INCREMENT PRIMARY KEY,
    nome_medico VARCHAR(60) NOT NULL,
    num_celular CHAR(11),
    email VARCHAR(80) NOT NULL,
    bairro VARCHAR(20) NOT NULL,
    rua CHAR(50) NOT NULL,
	num_residencia CHAR(10) NOT NULL,
    complemento VARCHAR(50),
    dt_nascimento DATE NOT NULL 
)
default charset = utf8;

CREATE TABLE IF NOT EXISTS secretaria (
	
    matricula_secretaria INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nome_secretaria VARCHAR(60) NOT NULL,
    num_celular CHAR(11) NOT NULL,
    email VARCHAR(80) NOT NULL,
    bairro VARCHAR(20) NOT NULL,
    rua CHAR(50) NOT NULL,
	num_residencia CHAR(10) NOT NULL,
    complemento VARCHAR(50),
    dt_nascimento DATE NOT NULL
)
default charset = utf8;

CREATE TABLE IF NOT EXISTS tipo_consulta (
	
    id_tipo INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	finalidade VARCHAR(20),
    valor DECIMAL(7,2)
)
default charset = utf8;

CREATE TABLE IF NOT EXISTS consulta (
	
	id_consulta INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    fk_matricula_medico INT NOT NULL,
    fk_animal INT NOT NULL,
    fk_cpf CHAR(11) NOT NULL,
	fk_tipo_consulta INT NOT NULL,
    dt_consulta DATE NOT NULL,
    hr_consulta TIME NOT NULL,
		
    FOREIGN KEY (fk_matricula_medico) REFERENCES medico(matricula_medico),
	FOREIGN KEY (fk_animal) REFERENCES animal(id_animal),
    FOREIGN KEY (fk_cpf) REFERENCES	cliente(id_cpf),
    FOREIGN KEY (fk_tipo_consulta) REFERENCES tipo_consulta(id_tipo)
)
default charset = utf8;

CREATE TABLE IF NOT EXISTS login (

    id_conta INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    fk_cpf CHAR(11) NOT NULL,
    fk_matricula_secretaria INT NOT NULL,
    fk_matricula_medico INT NOT NULL,
    usuario VARCHAR(20) NOT NULL,
    senha VARCHAR(10) NOT NULL,

    FOREIGN KEY (fk_cpf) REFERENCES	cliente(id_cpf),
    FOREIGN KEY (fk_matricula_secretaria) REFERENCES secretaria(matricula_secretaria),
    FOREIGN KEY (fk_matricula_medico) REFERENCES medico(matricula_medico)
)
default charset = utf8;

CREATE TABLE IF NOT EXISTS historico (

    id_historico INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    fk_animal INT NOT NULL,
    fk_tipo INT NOT NULL,
    fk_cpf CHAR(11) NOT NULL,
    fk_consulta INT NOT NULL,
    remedio VARCHAR(40) NOT NULL,
    diagnostico VARCHAR(40) NOT NULL,

    FOREIGN KEY (fk_animal) REFERENCES animal(id_animal),
    FOREIGN KEY (fk_tipo) REFERENCES tipo_consulta(id_tipo),
    FOREIGN KEY (fk_cpf) REFERENCES	cliente(id_cpf),
    FOREIGN KEY (fk_consulta) REFERENCES consulta(id_consulta)
    
)
default charset = utf8;

