from datetime import datetime
from conectionsdb import *
from config import *
import os

while True:
    print("\n-- Agenda de Tarefas --")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Calendario")
    print("0. Sair")
    opcao = input("Digite a opção desejada: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        opcao2 = int(input("Você deseja ordernar por:\n[1]Data/hora\n[2]Data Especifica\n[3]ID\nOpção desejada: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        if opcao2 == 1:
            # data = input("Digite a data (DD/MM/AAAA): ")
            # hora = input("Digite a hora (HH:MM): ")
            listar_tarefas_ordenadas()
            opcao3 = input("[1]Editar  [2]Excluir  [3]Sair\nOpção: ")
            if opcao3 == "1":
                print("em andamento")
            elif opcao3 == "2":
                apagar_tarefa()
            elif opcao3 == "3":
                print("em andamento")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Opção Invalida")
        elif opcao2 == 2:
            print("em andamento")
        else:
            listar_tarefas()
            opcao3 = input("[1]Editar  [2]Excluir  [3]Sair\nOpção: ")
            if opcao3 == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("em andamento")
            elif opcao3 == "2":
                apagar_tarefa()
            elif opcao3 == "3":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("em andamento")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Opção Invalida")

    elif opcao == "3":
        apagar_tarefa()
    elif opcao == "0":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Encerrando programa...")
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opção inválida.")
