from pymongo import MongoClient

def get_database():
    CONNECTION_STRING = "mongodb+srv://Kirito:Jangoss.123654789@cluster0.va5nn.mongodb.net/bot-mascotinho?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    return client['Trabalho']

db = get_database()
collection_name = db["tarefas"]