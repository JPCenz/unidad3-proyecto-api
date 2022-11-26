from pymongo import MongoClient
import requests as rq

client = MongoClient('localhost', 27017)
# vamos a conectar a una db
db = client["ricky_and_morty"]

for i in range(1,22):
    try:
        u = 'https://rickandmortyapi.com/api/character'
        response = rq.get(url=u,params={'page':i})
        data = response.json()
        for c in data['results']:
            db.character.insert_one(c)
            print("insertado")
    except Exception as ex:
            print(ex)

print('OBJETOS CREADOS ok')
            




