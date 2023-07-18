create database if not exists cadastro;
-- drop database cadastro;
use cadastro;

-- criação da tabela de usuários --

create table usuario(
	IdUsuario int auto_increment,
    Username varchar(20) not null,
    Email varchar(100) not null,
    Senha varchar(20) not null,
    Confirma_Senha varchar(20) not null,
    constraint pk_IdUsuario primary key (IdUsuario)
);

show tables;
desc usuario;