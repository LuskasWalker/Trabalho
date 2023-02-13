#Datas
from datetime import datetime

class Tarefa:#Cria a classe Tarefas
    def __init__(self, tar_id, nome, data, hora):#Inicia a função com construtor Init(Serve para criar os objetos da classe)
        self.nome = nome
        self.tar_id = tar_id
        self.data = datetime.strptime(data, '%d/%m/%Y')
        self.hora = datetime.strptime(hora, '%H:%M')
        
#Comando para adicionar tarefas
def adicionar_tarefa():
    nome = input("Digite o nome da tarefa: ")
    data = input("Digite a data da tarefa (DD/MM/AAAA): ")
    hora = input("Digite a hora da tarefa (HH:MM): ")
    tar_id =+ 1
    #Verificando se a data inserida é valida, ou seja, maior que a data atual
    data_obj = datetime.strptime(data, "%d/%m/%Y")
    data_atual = datetime.now()
    if data_obj < data_atual:
        print("A data fornecida é inválida")
    else:
        #tratamento de erro
        try:
            tarefa = Tarefa(tar_id, nome, data, hora)
            tarefas.append(tarefa)
            print("Tarefa adicionada com sucesso.")
        except:
            print('Data ou hora invalida, por favor tente novamente')

#Comando para listar tarefas
def listar_tarefas(data=None, hora=None):
    #Verificando se há tarefas na lista
    if not tarefas:
        print("Não há tarefas cadastradas.")
    else:
        #Filtrando as pesquisas
        tarefas_filtradas = tarefas
        if data:#Verifica se há argumentos de datas
            data_filtrada = datetime.strptime(data, '%d/%m/%Y')#Converte em objetos de dia/mes/ano
            #lambda é passada como argumento para o método filter para verificar se a data da tarefa é igual à data filtrada.
            tarefas_filtradas = filter(lambda t: t.data == data_filtrada, tarefas_filtradas)
        if hora:
            hora_filtrada = datetime.strptime(hora, '%H:%M')#Converte em objetos de data/hora
            #lambda é passada como argumento para o método filter para verificar se a data da tarefa é igual à data filtrada.
            tarefas_filtradas = filter(lambda t: t.hora == hora_filtrada, tarefas_filtradas)
        for tarefa in tarefas_filtradas:
            data_formatada = tarefa.data.strftime('%d/%m/%Y')
            hora_formatada = tarefa.hora.strftime('%H:%M')
            print(f"{tarefa._id } - {tarefa.nome}({data_formatada} às {hora_formatada})")
            
def apagar_tarefa():
    # Pede ao usuário que forneça o número da tarefa que deseja apagar
    num_tarefa = int(input("Digite o número da tarefa que deseja apagar: "))

    # Verificar se o número da tarefa é válido
    if num_tarefa < 1 or num_tarefa > len(tarefas):
        print("Número de tarefa inválido.")
    else:
        # Remover a tarefa da lista
        tarefa_apagada = tarefas.pop(num_tarefa - 1)
        print(f"A tarefa '{tarefa_apagada}' foi apagada com sucesso.")

tar_id = 0
tarefas = []
data_atual = datetime.now().date().strftime('%d/%m/%Y')

#Menu de interação
while True:
    print("\n-- Agenda de Tarefas --")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("0. Sair")
    opcao = input("Digite a opção desejada: ")
    #verifica as interações
    if opcao == "1":
        adicionar_tarefa()#Inicia a função Adicionar Tarefas
    elif opcao == "2":
        data = input("Digite a data (DD/MM/AAAA): ")#Argumento para filtro
        hora = input("Digite a hora (HH:MM): ")#Argumento para filtro
        listar_tarefas(data, hora)#Inicia a função listar tarefas com filtro
    elif opcao == "0":
        print("Encerrando programa...")#Encerra o programa
        break
    else:
        print("Opção inválida.")#tratamento de erro