import customtkinter as ctk
from tkinter import *
import mysql.connector
from tkinter import messagebox

#Configuração de aparência
ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")


#Conexão com banco de dados (tabela já criada)
class banco_dados():
    def conexao_db(self):
        self.conexao = mysql.connector.connect(
            host='',
            user='',
            password='',
            database='cadastro',
        )
        self.cursor = self.conexao.cursor()
        print('Banco conectado.')

    # Função para desconectar banco de dados
    def desconectar_db(self):
        self.cursor.close()
        self.conexao.close()
        print('Banco desconectado.')

    # Função para cadastrar usuário no banco de dados
    def cadastrar_usuario(self):
        self.userCadastro = self.username_cadastro.get()
        self.userEmail = self.email_cadastro.get()
        self.userSenha = self.senha_cadastro.get()
        self.userConfirma_Senha = self.confirma_senha.get()

        self.conexao_db()

        insert_query = """ INSERT INTO usuario (Username, Email,Senha,Confirma_Senha)
        VALUES (%s, %s, %s, %s)
        """
        self.cursor.execute(insert_query,(self.userCadastro, self.userEmail,self.userSenha,self.userConfirma_Senha))

        # Verificação dos campos
        try:
            if (self.userCadastro == '' or self.userEmail == '' or self.userSenha == '' or self.userConfirma_Senha == ''):
                messagebox.showerror(title='Sistema de cadastro', message='Preencha todos os campos!')
            elif (len(self.userSenha) < 6):
                messagebox.showwarning(title='Sistema de cadastro', message='A senha deve ter no mínimo 6 caracteres!')
            elif (self.userSenha != self.userConfirma_Senha):
                messagebox.showwarning(title='Sistema de cadastro', message='As senhas não são iguais!')
            else:
                self.conexao.commit()
                messagebox.showinfo(title='Sistema de cadastro', message='Cadastro realizado com sucesso!')
                self.desconectar_db()
                self.limpa_campos_cadastro()
        except:
            messagebox.showerror(title='Sistema de cadastro', message='Erro de processamento!')
            self.desconectar_db()

    # Função para efetuar login
    def verificar_login(self):
        self.loginUser = self.username_login.get()
        self.loginSenha = self.senha_login.get()


        self.conexao_db()

        selecao_query = "SELECT * FROM usuario WHERE (Username = %s AND Senha = %s)"

        self.cursor.execute(selecao_query, (self.loginUser, self.loginSenha))

        self.verificar_dados = self.cursor.fetchone() #pecorrer a tabela usuario

        # Verificação dos campos com banco de dados
        try:
            if (self.loginUser == '' or self.loginSenha == ''):
                messagebox.showwarning(title='Sistema de login', message='Preencha todos os campos!')
            elif (self.loginUser in self.verificar_dados and self.loginSenha in self.verificar_dados):
                messagebox.showinfo(title="Sistema de login", message='Login efetuado!')
                self.desconectar_db()
                self.limpa_campos_login()
        except:
            messagebox.showwarning(title='Sistema de login', message='Usuário ou senha não cadastrado!')
            self.desconectar_db()


class App(ctk.CTk, banco_dados):
    def __init__(self):
        super().__init__()
        self.config_TelaPrincipal()
        self.tela_login()
        self.conexao_db()


    # Configuração da Janela principal
    def config_TelaPrincipal(self):
        largura = 500
        altura = 400
        self.geometry(f'{largura}x{altura}')
        self.title('Tela de login')
        self.resizable(False,False) # determinar tamanho fixo da tela

    def tela_login(self):

        self.title = ctk.CTkLabel(self, text='Faça o seu login ou Cadastre-se!', font=('Roboto bold', 14))
        self.title.grid(row=0, column=0, padx=150,pady=10)

        # Formulário de Login
        self.frame_login = ctk.CTkFrame(self, width=500, height=400)
        self.frame_login.place(x=90, y=50)

        self.lb_title = ctk.CTkLabel(self.frame_login, text='Tela de Login',font=('Roboto bold', 22))
        self.lb_title.pack(padx=10, pady=20)

        self.username_login = ctk.CTkEntry(self.frame_login, width=300, placeholder_text='Usuário', font=('Roboto bold', 14))
        self.username_login.pack(padx=10, pady=10)
        self.senha_login = ctk.CTkEntry(self.frame_login, width=300, placeholder_text='Senha', show='*', font=('Roboto bold', 14))
        self.senha_login.pack(padx=10, pady=10)

        self.btn_login = ctk.CTkButton(self.frame_login, width=150, text='Login'.upper(), font=('Roboto bold', 14), corner_radius=15, command=self.verificar_login)
        self.btn_login.pack(padx=10, pady=10)

        self.spam = ctk.CTkLabel(self.frame_login, text='Se não tem conta, cadastre-se!',font=('Roboto', 12))
        self.spam.pack(padx=10, pady=10)

        self.btn_cadastro = ctk.CTkButton(self.frame_login, width=150, text='Cadastre-se'.upper(), font=('Roboto bold', 14),corner_radius=15, fg_color='green', command=self.tela_cadastro)
        self.btn_cadastro.pack(padx=10, pady=10)

    def tela_cadastro(self):
        # Remover tela de Login
        self.frame_login.place_forget()
    # Tela de Cadastro
        self.frame_cadastro = ctk.CTkFrame(self, width=500, height=400)
        self.frame_cadastro.place(x=90, y=50)

        self.lb_title = ctk.CTkLabel(self.frame_cadastro, text='Tela de Cadastro', font=('Roboto bold', 22))
        self.lb_title.pack(padx=10, pady=10)

        self.username_cadastro = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text='Digite um usuário',font=('Roboto bold', 14))
        self.username_cadastro.pack(padx=10, pady=5)
        self.email_cadastro = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text='Digite seu email',font=('Roboto bold', 14))
        self.email_cadastro.pack(padx=10, pady=5)
        self.senha_cadastro = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text='Digite uma senha', show='*', font=('Roboto bold', 14))
        self.senha_cadastro.pack(padx=10, pady=5)
        self.confirma_senha = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text='Confirme a senha', show='*',font=('Roboto bold', 14))
        self.confirma_senha.pack(padx=10, pady=5)

        self.ver_senha = ctk.CTkCheckBox(self.frame_cadastro, text='Clique para ver a senha', font=('Roboto', 12))
        self.ver_senha.pack(padx=10)

        self.btn_cadastrar = ctk.CTkButton(self.frame_cadastro, width=150, text='Cadastrar'.upper(),font=('Roboto bold', 14), corner_radius=15, fg_color='green', command=self.cadastrar_usuario)
        self.btn_cadastrar.pack(padx=10, pady=10)

        self.btn_voltar_login = ctk.CTkButton(self.frame_cadastro, width=150, text='Fazer Login'.upper(), font=('Roboto bold', 14),corner_radius=15, fg_color='#444',hover_color='#333', command=self.tela_login)
        self.btn_voltar_login.pack(padx=10)

    def limpa_campos_cadastro(self):
        self.username_cadastro.delete(0, END)
        self.email_cadastro.delete(0, END)
        self.senha_cadastro.delete(0, END)
        self.confirma_senha.delete(0, END)

    def limpa_campos_login(self):
        self.username_login.delete(0, END)
        self.senha_login.delete(0, END)




if __name__ == '__main__':
    app = App()
    app.mainloop()

