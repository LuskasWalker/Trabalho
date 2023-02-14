from datetime import datetime
import calendar

class Tarefa:
    def __init__(self, tar_id, nome, data, hora):
        self.nome = nome
        self.tar_id = tar_id
        self.data = datetime.strptime(data, '%d/%m/%Y')
        self.hora = datetime.strptime(hora, '%H:%M')
        
def adicionar_tarefa():
    nome = input("Digite o nome da tarefa: ")
    data = input("Digite a data da tarefa (DD/MM/AAAA): ")
    hora = input("Digite a hora da tarefa (HH:MM): ")
    tar_id =+ 1
    try:
        tarefa = Tarefa(tar_id, nome, data, hora)
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso.")
    except:
        print('Data ou hora invalida, por favor tente novamente')

def print_calendario():
    ano = 2023
    mes = 2

    print(calendar.month(ano, mes))

#Comando para listar tarefas
def listar_tarefas(data=None, hora=None):

    if not tarefas:
        print("Não há tarefas cadastradas.")
    else:
        tarefas_filtradas = tarefas
        if data:
            data_filtrada = datetime.strptime(data, '%d/%m/%Y')

            tarefas_filtradas = filter(lambda t: t.data == data_filtrada, tarefas_filtradas)
        if hora:
            hora_filtrada = datetime.strptime(hora, '%H:%M')
            tarefas_filtradas = filter(lambda t: t.hora == hora_filtrada, tarefas_filtradas)
        for tarefa in tarefas_filtradas:
            data_formatada = tarefa.data.strftime('%d/%m/%Y')
            hora_formatada = tarefa.hora.strftime('%H:%M')
            print(f"{tarefa.tar_id } - {tarefa.nome}({data_formatada} às {hora_formatada})")
            
def apagar_tarefa():
    # Pede ao usuário que forneça o número da tarefa que deseja apagar
    num_tarefa = int(input("Digite o número da tarefa que deseja apagar: "))

    if num_tarefa < 1 or num_tarefa > len(tarefas):
        print("Número de tarefa inválido.")
    else:
        tarefa_apagada = tarefas.pop(num_tarefa - 1)
        print(f"A tarefa '{tarefa_apagada}' foi apagada com sucesso.")

tar_id = 0
tarefas = []
data_atual = datetime.now().date().strftime('%d/%m/%Y')

while True:
    print("\n-- Agenda de Tarefas --")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Calendario")
    print("0. Sair")
    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        data = input("Digite a data (DD/MM/AAAA): ")
        hora = input("Digite a hora (HH:MM): ")
        listar_tarefas(data, hora)
    elif opcao == "3":
        print_calendario()
    elif opcao == "0":
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida.")