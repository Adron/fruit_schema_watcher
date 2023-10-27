import datetime

from pymongo import MongoClient


def fetch_collections_and_properties(db):
    collection_names = db.list_collection_names()

    collections_and_properties = {}

    for collection_name in collection_names:
        collection = db[collection_name]
        properties_set = set()

        for document in collection.find():
            properties_set.update(document.keys())

        collections_and_properties[collection_name] = list(properties_set)

    return collections_and_properties

if __name__ == "__main__":
    # Connect to MongoDB
    client = MongoClient('mongodb://root:examplepass@localhost:27017')
    db = client['test']

    start_time = datetime.datetime.now()
    print(f"Process started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

    # Fetch collections and their properties
    result = fetch_collections_and_properties(db)
    for collection, properties in result.items():
        print(f"Collection: {collection}")
        print(f"Properties: {', '.join(properties)}\n")

    # update GraphQL Server here.

    # Close the connection
    client.close()

    end_time = datetime.datetime.now()
    print(f"Process ended at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    time_elapsed = end_time - start_time
    print(f"Time elapsed: {time_elapsed}")