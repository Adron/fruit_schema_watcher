from pymongo import MongoClient

def createDocument():
    # Connect to the MongoDB instance
    client = MongoClient('mongodb://root:examplepass@localhost:27017')
    db = client['test']

    # Define the document to be inserted
    document = {
        'special_message': "Hello, this is a greeting from this fruit product! Enjoy!"
    }

    # Insert the document into the collection
    db.the_hello_world_collection.insert_one(document)

# Call the function to create the document
createDocument()
