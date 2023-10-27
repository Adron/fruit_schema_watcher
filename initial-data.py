from pymongo import MongoClient

client = MongoClient('mongodb://root:examplepass@localhost:27017')

db = client['test']
users = db['users']
the_first_collection = db['the_first_collection']

users.insert_one({'name': 'John', 'age': 30})

the_first_collection.insert_many([
    {'bank': 'PNC'},
    {'bank': 'Citibank'},
    {'bank': 'Bank of America'},
    {'bank': 'First Bank'}
])

client.close()