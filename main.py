import sys
import os
from banco import inicializar_banco
from usuarios import menu_usuarios
from registros_diarios import criar_registro, ler_registros, ler_um, atualizar_registro, deletar_registro
from relatorio import relatorio_por_usuario
from habitos import menu_habitos


sys.path.insert(0, os.path.dirname(__file__)) 


inicializar_banco()

def menu_principal():
    while True:
        print("_" * 35)
        print(" Sistema de Habitos Saudaveis ")
        print("-" * 35)
        print(" 1 - Dados do Usuario")
        print(" 2 - Dados de Habitos")
        print(" 3 - Registros Diários ")
        print(" 4 - Relatório")
        print(" 5 - Sair")
        escolha = input(" \nEscolha uma opção: ")

        if escolha == "1":
          menu_usuarios()
         
        elif escolha == "2":
          menu_habitos()

        elif escolha == "3":
          while True:
            print("\n======================= Registros Diarios =======================\n")
            print(" 1 - Criar novo registro")
            print(" 2 - Ler todos os registros")
            print(" 3 - Ler um registro específico")
            print(" 4 - Atualizar registro")
            print(" 5 - Deletar um registro")
            print(" 6 - Voltar")

            opcao = input("\nEscolha uma opção: ")
   #quero colocar mais possibilidades de respostas e ver ser coloco esse menu no arquivo de registros          
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
               print("===============================================================\n") #tem 63 '='
               break
            else:
               print("\nOpção inválida!")
               

        elif escolha == "4":
          print("\nRelatorio")
          relatorio_por_usuario()

        elif escolha == "5":
          print("\nSaindo do sistema")
          break
        else:
          print(" Opção inválida. Tente novamente.") 

if __name__ == "__main__":
    menu_principal()