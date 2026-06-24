import sys
import os
from banco import inicializar_banco
from usuarios import menu_usuarios
from registros_diarios import (
    criar_registro,
    ler_registros,
    ler_um,
    atualizar_registro,
    deletar_registro
)
from relatorio import menu_relatorios
from habitos import menu_habitos

sys.path.insert(0, os.path.dirname(__file__))

inicializar_banco()

def menu_principal():
    while True:
        print("_" * 35)
        print(" Sistema de Hábitos Saudáveis ")
        print("-" * 35)
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
            while True:
                print("\n======================= Registros Diários =======================\n")
                print(" 1 - Criar novo registro")
                print(" 2 - Ler todos os registros")
                print(" 3 - Ler um registro específico")
                print(" 4 - Atualizar registro")
                print(" 5 - Deletar um registro")
                print(" 6 - Voltar")

                opcao = input("\nEscolha uma opção: ").strip()

                if opcao == "1":
                    criar_registro()
                    print("===============================================================\n")

                elif opcao == "2":
                    ler_registros()
                    print("===============================================================\n")

                elif opcao == "3":
                    ler_um()
                    print("===============================================================\n")

                elif opcao == "4":
                    atualizar_registro()
                    print("===============================================================\n")

                elif opcao == "5":
                    deletar_registro()
                    print("===============================================================\n")

                elif opcao == "6":
                    print("Voltando ao menu principal.")
                    print("===============================================================\n")
                    break

                else:
                    print("\nOpção inválida!")

        elif escolha == "4":
            menu_relatorios()

        elif escolha == "5":
            print("\nSaindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
    