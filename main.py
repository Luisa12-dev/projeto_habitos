import sys
import os
from banco import inicializar_banco
from usuarios import menu_usuarios
from registros_diarios import menu_registros
from relatorio import menu_relatorios
from habitos import menu_habitos

sys.path.insert(0, os.path.dirname(__file__))

inicializar_banco()

def menu_principal():
    while True:
        print("===============================================================================")
        print("                            Sistema de Hábitos Saudáveis                       ")
        print("===============================================================================\n")
        print(" 1 - Dados do Usuário")
        print(" 2 - Dados de Hábitos")
        print(" 3 - Registros Diários")
        print(" 4 - Relatórios")
        print(" 5 - Sair")

        escolha = input("\nEscolha uma opção: ").strip()

        if escolha == "1":
            menu_usuarios()

        elif escolha == "2":
            menu_habitos()

        elif escolha == "3":
            menu_registros()
            
        elif escolha == "4":
            menu_relatorios()

        elif escolha == "5":
            print("\nLembre-se: para todo hábito, manter a constância é essencial!")
            print("\nSaindo do sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
    