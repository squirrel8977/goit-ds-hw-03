from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Вкажіть ваш MongoDB URI
client = MongoClient("mongodb+srv://marypetr:tFEM5eG1ZBn03A5H@cluster0.evtec.mongodb.net/", server_api=ServerApi('1'))
# Створення або підключення до бази даних
db = client["mydatabase"]

# Створення або підключення до колекції
collection = db["cats"]
cats = [
    {"name": "murchik", "age": 3, "features": ["ходить в капці", "дає себе гладити", "рудий"]},
    {"name": "sunny", "age": 5, "features": ["чорний", "грайливий", "не любить собак"]},
    {"name": "vaska", "age": 7, "features": ["білий", "любит гладитись", "спить на ліжку"]},
    {"name": "rocky", "age": 2, "features": ["пухнастий", "сірий", "дуже гучний"]},
    {"name": "balboa", "age": 1, "features": ["рудий", "дуже активний", "любит гратись"]},
    {"name": "simba", "age": 3, "features": ["старий", "мудрий", "повільний"]},
]
# Додавання документа до колекції

collection.insert_many(cats)

print("База даних та колекція створені успішно!")

