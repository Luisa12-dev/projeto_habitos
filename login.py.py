
import sqlite3

def casdastro():
 email= input("Digite seu email: ")
 nome = input("Digite seu nome: ")
 senha = input("Digite a senha: ")

conexao = sqlite3.connect("usuarios")
buscar = conexao.busca()

busca.execute(
    "INSERT INTO usuarios(usuario, nome, senha) VALUES (?, ?,?)",
    (emeil,nome, senha)
)

conexao.commit()
conexao.close()

print("Usuário cadastrado!")

import sqlite3

usuario_id = input("Usuário: ")
nome = input("Nome: ")
senha = input("Senha: ")

conexao = sqlite3.connect("usuarios")
buscar= conexao.buscar()

buscar.execute(
    "SELECT * FROM usuarios WHERE usuario=? AND senha=?",
    (usuario, senha)
)

pesquisa = buscar.fetchone()

if pesquisa:
    print("Login realizado com sucesso!")
else:
    print("Usuário ou senha incorretos.")

conexao.close()

