from pymongo import MongoClient

client = MongoClient('localhost', 27017)

# vamos a conectar a una db
db = client["ricky_and_morty"]
