from flask import Flask
from flask_graphql import GraphQLView
from pymongo import MongoClient
import graphene
from graphene import ObjectType

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['your_database_name']

class Query(ObjectType):
    pass

# Dynamically create GraphQL fields based on MongoDB collections and their properties
for collection_name in db.list_collection_names():
    collection = db[collection_name]
    document = collection.find_one()
    if document:
        fields = {key: graphene.String() for key in document.keys()}
        # Create a dynamic GraphQL ObjectType for each collection
        collection_type = type(collection_name.capitalize(), (ObjectType,), fields)
        setattr(Query, collection_name, graphene.Field(collection_type, id=graphene.String()))

        def resolver(self, info, id):
            return db[collection_name].find_one({"_id": id})

        setattr(Query, f"resolve_{collection_name}", resolver)

schema = graphene.Schema(query=Query)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run()
