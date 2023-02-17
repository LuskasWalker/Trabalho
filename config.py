from datetime import datetime
from conectionsdb import *
from bson.objectid import ObjectId
import os

class Tarefa:
    def __init__(self, id, nome, data_inicial, data_final, hora_inicial, hora_final, descricao):
        self.id = id
        self.nome = nome
        self.data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y')
        self.data_final = datetime.strptime(data_final, '%d/%m/%Y')
        self.hora_inicial = datetime.strptime(hora_inicial, '%H:%M')
        self.hora_final = datetime.strptime(hora_final, '%H:%M')
        self.descricao = descricao
        

def get_ultimo_id():
    id_documento = "63ee588d11cca8952689382f"
    id_config = collection_name.find_one({'_id': ObjectId(id_documento)})
    final_id = id_config["last_id"]
    return final_id

def adicionar_tarefa():
    nome = input("Digite o nome da tarefa: ")
    data_inicial = input("Digite o dia em que a tarefa ira começar (DD/MM/AAAA): ")
    data_final = input("Digite o dia em que a tarefa ira final (DD/MM/AAAA): ")
    hora_inicial = input("Digite a hora em que o evento ira começar (HH:MM): ")
    hora_final = input("Digite a hora em que o evento ira terminar (HH:MM): ")
    descricao_tarefas = input("Digite a descrição da Tarefa: ")
    try:
        ultimo_id = get_ultimo_id()
        novo_id = ultimo_id + 1
        print(novo_id)
        tarefa = Tarefa(novo_id, nome, data_inicial, data_final, hora_inicial, hora_final, descricao_tarefas)
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso.")
        os.system('cls' if os.name == 'nt' else 'clear')
        id_documento = "63ee588d11cca8952689382f"
        collection_name.find_one_and_update({"_id" : ObjectId(id_documento)} , { "$set" : {"last_id" : novo_id}})
        dado = {
        "_id" : novo_id,
        "nome" : f"{nome}",
        "data_inicial" : f"{data_inicial}",
        "data_final" : f"{data_final}",
        "hora_inicial" : f"{hora_inicial}",
        "hora_final" : f"{hora_final}",
        "descricao_tarefas" : f"{descricao_tarefas}"
        }
        collection_name.insert_many([dado])
    except Exception as e:
        print(e)
        print("Data ou hora invalida, por favor tente novamente")
        print("Leve em consideração ler o manual")

def listar_tarefas():
    if not collection_name.find({"_id": {"$gt": 0}}):
        return print('Não possui tarefas cadastradas')
    print("--Tarefas Ordenadas por ID--")
    for document in collection_name.find({"_id": {"$gt": 0}}):
        indentify = document["_id"]
        nome = document["nome"]
        data_list = document["data_inicial"]
        hora_list = document["hora_inicial"] 
        print(f"{indentify} - {nome}({data_list} as {hora_list})")

def listar_tarefas_ordenadas():
    if not collection_name.find({"_id": {"$gt": 0}}):
        return print('Não possui tarefas cadastradas')
    print("--Tarefas Ordenadas por Data e Hora--")
    tarefas = []
    for document in collection_name.find({"_id": {"$gt": 0}}):
        tarefas.append(document)
    n = len(tarefas)
    for i in range(n):
        for j in range(0, n-i-1):
            d1 = datetime.strptime(tarefas[j]["data_inicial"] + " " + tarefas[j]["hora_inicial"], "%d/%m/%Y %H:%M")
            d2 = datetime.strptime(tarefas[j+1]["data_inicial"] + " " + tarefas[j+1]["hora_inicial"], "%d/%m/%Y %H:%M")
            if d1 > d2:
                tarefas[j], tarefas[j+1] = tarefas[j+1], tarefas[j]
    for document in tarefas:
        identificador = document["_id"]
        nome = document["nome"]
        data_list = document["data_inicial"]
        hora_list = document["hora_inicial"] 
        print(f"{identificador} - {nome} ({data_list} às {hora_list})")

def apagar_tarefa(): 
    num_tarefa = int(input("Digite os IDs das tarefas que deseja apagar: "))
    tarefas = []
    for document in collection_name.find({"_id": {"$gt": 0}}):
        tarefas.append(document)
    if collection_name.find_one_and_delete({"_id" : num_tarefa,}):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"A tarefa 'ID = {num_tarefa}' foi apagada com sucesso.")
    else:
        print("Número de tarefa inválido.")
tarefas = []
data_atual = datetime.now().date().strftime('%d/%m/%Y')