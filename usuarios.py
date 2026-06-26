import sqlite3
from banco import conectar
from datetime import date

#conexao = sqlite3.connect("banco.db")

def cadastrar():
    conexao = conectar()
    cursor = conexao.cursor()

    print("\n============================ CADASTRAR USUÁRIO ============================\n")

    nome = input("\nNome: ")

    while nome == "":
        nome = input("Nome: ")

    email = input("\nEmail: ")

    while "@" not in email:
        print("\nEmail inválido.")
        email = input("Email: ")

    data_cadastro = date.today()

    cursor.execute("""
        INSERT INTO usuarios(nome,email,data_cadastro)
        VALUES(?,?,?)
    """, (nome, email, data_cadastro))

    conexao.commit()

    print("Usuário cadastrado com sucesso!")


def listar_usuarios():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM usuarios
    """)
    usuarios = cursor.fetchall()

    if len(usuarios) == 0:
        print("\nNenhum usuário cadastrado.")
        return

    print("\nUSUÁRIOS CADASTRADOS")

    print("ID   Nome                      Email                               Cadastro")
 
    print("-")

    for usuario in usuarios:
        print(f"{usuario[0]:<5}{usuario[1]:<25}{usuario[2]:<35}{usuario[3]}")

    print("-")


def editar_usuario():
    conexao = conectar()
    cursor = conexao.cursor()

    listar_usuarios()

    try:
        id_usuario = int(input("Digite o ID: "))
    except ValueError:
        print("ID inválido.")
        return

    cursor.execute(""" SELECT * FROM usuarios WHERE id = ?""", (id_usuario,))

    usuario = cursor.fetchone()

    if usuario is None:
        print("Usuário não encontrado.")
        return

    print("Pressione ENTER para manter o valor atual.")

    novo_nome = input(f"Nome ({usuario[1]}): ")

    if novo_nome == "":
        novo_nome = usuario[1]

    novo_email = input(f"Email ({usuario[2]}): ")

    if novo_email == "":
        novo_email = usuario[2]

    while "@" not in novo_email:
        print("Email inválido.")
        novo_email = input("Novo email: ")

        if novo_email == "":
            novo_email = usuario[2]
            break

    cursor.execute("""
        UPDATE usuarios
        SET nome = ?, email = ?
        WHERE id = ?
    """, (novo_nome, novo_email, id_usuario))

    conexao.commit()

    print("Usuário atualizado com sucesso!")


def deletar_usuario():
    conexao = conectar()
    cursor = conexao.cursor()

    listar_usuarios()

    try:
        id_usuario = int(input("Digite o ID para excluir: "))
    except ValueError:
        print("ID inválido.")
        return

    cursor.execute("""
        SELECT * FROM usuarios
        WHERE id = ?
    """, (id_usuario,))

    usuario = cursor.fetchone()

    if usuario is None:
        print("Usuário não encontrado.")
        return

    confirmar = input(f"Tem certeza que deseja excluir '{usuario[1]}'? (S/N): ").upper()

    if confirmar == "S": #aqui tinha um errinho. Estava != "S", mudei para == "S1"
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
        conexao.commit()
        print("\n[Sucesso] Usuário removido do sistema.")
    else:
        print("Operação cancelada.")
      

    
    
    conexao.commit()

    print("Usuário excluído com sucesso!")

def menu_usuarios():
    conexao = conectar()
    cursor = conexao.cursor()
    while True:

        print("\n============================= MENU DO USUÁRIO ============================\n")
        print(" 1 - Cadastrar usuário")
        print(" 2 - Listar usuários")
        print(" 3 - Editar usuário")
        print(" 4 - Deletar usuário")
        print(" 0 - Voltar")

        opcao = input("\nEscolha uma opção : ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            editar_usuario()
        elif opcao == "4":
            deletar_usuario()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

    if __name__ == "__main__":
     menu_usuarios()
     conexao.close()