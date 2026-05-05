CREATE DATABASE IF NOT EXISTS db_dogtor
default character set utf8
default collate utf8_general_ci;

CREATE TABLE IF NOT EXISTS cliente (
	
    id_cpf CHAR(11) NOT NULL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(80)NOT NULL,
    num_celular CHAR(11) NOT NULL,
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
    genero_animal CHAR(1),
    especie VARCHAR(15) NOT NULL,
    raca VARCHAR(15)NOT NULL,
	peso_animal DECIMAL(5,2),
    
    FOREIGN KEY (fk_cpf) REFERENCES cliente(id_cpf)
    
) 
default charset = utf8;

CREATE TABLE IF NOT EXISTS medico ( 
	
    matricula_medico INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nome_medico VARCHAR(60) NOT NULL,
    num_celular CHAR(11) NOT NULL,
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
	
	id_consulta int AUTO_INCREMENT NOT NULL PRIMARY KEY,
    fk_matricula_medico INT NOT NULL,
    fk_animal INT NOT NULL,
    fk_cpf CHAR(11) NOT NULL,
	fk_finalidade VARCHAR(20),
    dt_consulta DATE NOT NULL,
    hora_consulta TIME NOT NULL,
		
    FOREIGN KEY (fk_matricula_medico) REFERENCES medico(matricula_medico),
	FOREIGN KEY (fk_animal) REFERENCES animal(id_animal),
    FOREIGN KEY (fk_cpf) REFERENCES	cliente(id_cpf),
    FOREIGN KEY (fk_finalidade) REFERENCES tipo_consulta(finalidade)
)
default charset = utf8;