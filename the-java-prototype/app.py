from aiohttp import web
from graphql import (
    GraphQLObjectType,
    GraphQLField,
    GraphQLString,
    GraphQLSchema
)
from aiohttp_graphql import GraphQLView

# Define the GraphQL type for the query
QueryType = GraphQLObjectType(
    name='Query',
    fields={
        'hello': GraphQLField(
            GraphQLString,
            resolve=lambda obj, info: "world"
        )
    }
)

# Create the GraphQL schema with the defined type
schema = GraphQLSchema(query=QueryType)

# Create the aiohttp web application
app = web.Application()

# Setup the GraphQL endpoint
GraphQLView.attach(
    app,
    schema=schema,
    graphiql=True,  # Enables the GraphiQL IDE
    path="/graphql"
)

# Run the aiohttp web server
if __name__ == '__main__':
    web.run_app(app, port=4000)
