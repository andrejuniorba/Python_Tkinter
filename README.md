# Interface Gráfica com Python


# Tela de Login e Cadastro com MySQL

Este projeto consiste em uma aplicação de Tela de Login e Tela de Cadastro utilizando a biblioteca Custom Tkinter em conjunto com o Tkinter padrão do Python. Além disso, foi utilizado o banco de dados MySQL no MySQL Workbench para armazenar os dados de cadastro dos usuários e garantir a persistência das informações.

## Tecnologias Utilizadas
- Custom Tkinter
- Tkinter
- MySQL

## Funcionalidades Implementadas
**Tela de Login**: Permite que os usuários registrados acessem a aplicação, fornecendo seus dados de login.

**Tela de Cadastro**: Permite que novos usuários se cadastrem no sistema, fornecendo informações como nome de usuário, senha, e-mail, etc.

**Banco de Dados MySQL**: Utilizamos o MySQL Workbench para criar o banco de dados que armazena os dados dos usuários cadastrados.

**Persistência de Dados**: Os dados inseridos na Tela de Cadastro são armazenados no banco de dados, garantindo que as informações permaneçam disponíveis mesmo após o encerramento da aplicação.

**Verificação de Acesso**: Através da Tela de Login, o sistema verifica se as credenciais inseridas pelo usuário correspondem aos registros no banco de dados, permitindo ou negando o acesso à aplicação.

## Imagens do Projeto
Aqui estão algumas imagens das telas do projeto:

Tela de Login:

<div align="center">
<img src="https://github.com/andrejuniorba/Python_Tkinter/assets/68282848/ec3dd110-f068-4d2a-b639-9460d4e51ad6" width="300px"/>
</div>

Tela de Cadastro:

<div align="center">
<img src="https://github.com/andrejuniorba/Python_Tkinter/assets/68282848/9b32b449-9ca0-4233-ad0f-ce261755ffdf" width="300px"/>
</div>

Banco de Dados no MySQL Workbench:

<div align="center">
<img src="https://github.com/andrejuniorba/Python_Tkinter/assets/68282848/8dc847fe-575c-4bce-849f-0288d47b878f" width="300px"/>
</div>

## Como Executar o Projeto
Para executar o projeto em sua máquina local, siga os passos abaixo:

- Clone o repositório para o seu ambiente local 

- Certifique-se de ter o Python instalado em sua máquina.

- Instale as bibliotecas necessárias: customtkinter e mysql-connector-python

- Importe o arquivo do banco de dados no MySQL Workbench e configure a conexão com o banco de dados na aplicação, atualizando as informações de conexão no código, como host, user e password.

Feito isso, você deverá ver a aplicação sendo executada e poderá interagir com as telas de login e cadastro.
