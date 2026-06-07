import sys
import os

sys.path.insert(0, os.path.dirname(__file__)) 

from banco import inicializar_banco

def menu_principal():
    print("_" * 25)
    print(" Sistema de Habitos Saudaveis ")
    print("-" * 25)

while True:
    print(" 1 - Cadastrar Usuario")
    print(" 2 - Cadastrar Habitos")
    print(" 3 - Registros Diarios ")
    print(" 4 - Relatorio")
    print(" 5 - Sair")
    escolha = input(" Escolha uma opção: ")

    if escolha == "1":
      print(" Usuario")
    elif escolha == "2":
      print(" Habitos")
    elif escolha == "3":
      print(" Registros Diarios")
    elif escolha == "4":
      print(" Relatorio")
    elif escolha == "5":
      print(" Saindo do sistema")
      break
    else:
      print(" Opção inválida. Tente novamente.") 
