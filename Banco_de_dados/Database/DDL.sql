CREATE DATABASE IF NOT EXISTS db_dogtor
default character set utf8
default collate utf8_general_ci;

use db_dogtor; -- Caso rode o script inteiro, para selecionar o banco de dados
 
CREATE TABLE IF NOT EXISTS cliente (
    
    cpf CHAR(11) NOT NULL PRIMARY KEY,
    nome_cliente VARCHAR(50) NOT NULL,
    email VARCHAR(80) NOT NULL,
    celular CHAR(11) NOT NULL,
    bairro VARCHAR(20),
    rua CHAR(100) ,
	numero CHAR(10) ,
    complemento VARCHAR(50) 
)
default charset = utf8;

CREATE TABLE IF NOT EXISTS animal (  

	id_animal INT AUTO_INCREMENT PRIMARY KEY,
    fk_cpf CHAR(11),
    nome_animal VARCHAR(30) NOT NULL,
    genero CHAR(1) NOT NULL,
    especie VARCHAR(15) NOT NULL,
    raca VARCHAR(15),
	peso DECIMAL(5,2) NOT NULL,
    
    FOREIGN KEY (fk_cpf) REFERENCES cliente(cpf)   
) 
default charset = utf8;

CREATE TABLE IF NOT EXISTS funcionarios (
    
    id_funcionario INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    fk_id_cargo INT,
    nome_funcionario VARCHAR(60) NOT NULL,
    num_celular CHAR(11) NOT NULL,
    email VARCHAR(80) NOT NULL,
    bairro VARCHAR(20) NOT NULL,
    rua CHAR(50) NOT NULL,
    complemento VARCHAR(50),
    dt_nascimento DATE NOT NULL,

    FOREIGN KEY (fk_id_cargo) REFERENCES cargo(id_cargo)
)
default charset = utf8;

CREATE TABLE IF NOT EXISTS cargo (

    id_cargo INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nome_cargo VARCHAR(20) NOT NULL
)
default charset = utf8;

CREATE TABLE IF NOT EXISTS login (

    id_login INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    fk_funcionario INT ,
    senha TEXT NOT NULL,
    fk_cpf CHAR(11) ,
    fk_cargo INT,

    -- Retirado o Not null das FK, pois elas podem ser nulas, o cliente não vai ter fk do funcionário e cargo por exemplos.

    FOREIGN KEY (fk_funcionario) REFERENCES funcionarios(id_funcionario),
    FOREIGN KEY (fk_cpf) REFERENCES cliente(cpf),
    FOREIGN KEY (fk_cargo) REFERENCES cargo(id_cargo)    
)
default charset = utf8;

CREATE TABLE IF NOT EXISTS tipo_consulta (
	
    id_consulta INT NOT NULL PRIMARY KEY,
	finalidade VARCHAR(20),
    valor DECIMAL(7,2)
)
default charset = utf8;

CREATE TABLE IF NOT EXISTS consulta (
	
	id_consulta INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    fk_funcionario INT,
    fk_animal INT NOT NULL,
    fk_cpf CHAR(11) ,
	fk_tipo_consulta INT NOT NULL,
    dt_consulta DATE NOT NULL,
    hr_consulta TIME NOT NULL,
    status VARCHAR(15) DEFAULT "EM ANDAMENTO",
		
    FOREIGN KEY (fk_funcionario) REFERENCES funcionarios(id_funcionario),
	FOREIGN KEY (fk_animal) REFERENCES animal(id_animal),
    FOREIGN KEY (fk_cpf) REFERENCES	cliente(cpf),
    FOREIGN KEY (fk_tipo_consulta) REFERENCES tipo_consulta(id_consulta)
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
    FOREIGN KEY (fk_cpf) REFERENCES	cliente(cpf),
    FOREIGN KEY (fk_consulta) REFERENCES consulta(id_consulta)
    
)
default charset = utf8;