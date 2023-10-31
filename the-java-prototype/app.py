from flask import Flask
from flask_graphql import GraphQLView
import graphene
from pymongo import MongoClient

app = Flask(__name__)

# Connect to the MongoDB instance
client = MongoClient('mongodb://root:examplepass@localhost:27017')
db = client['test']

class Query(graphene.ObjectType):
    special_message = graphene.String()

    def resolve_special_message(self, info):
        # Fetch the message from the MongoDB collection
        document = db.the_hello_world_collection.find_one()
        if document:
            return document.get('special_message')
        return "Message not found"

schema = graphene.Schema(query=Query)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(debug=True)
