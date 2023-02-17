from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

def get_database():
    CONNECTION_STRING = os.getenv("DATABASE_URL")
    client = MongoClient(CONNECTION_STRING)
    return client['Trabalho']

db = get_database()
collection_name = db["tarefas"]