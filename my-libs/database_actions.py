from word_generator import generate_readable_word
from word_generator import random_collection_collateral
from pymongo import MongoClient

def the_deluge_of_chaos():
    mongo_collection = generate_readable_word(5)
    collection_document = random_collection_collateral()

    client = MongoClient('mongodb://root:examplepass@localhost:27017')
    db = client['test']

    db.create_collection(mongo_collection)
    collection = db[mongo_collection]
    print(mongo_collection + " has been created.")

    collection_document = eval(collection_document)

    collection.insert_one(collection_document)
    print(collection_document)
    print("...has been created.")

    client.close()
