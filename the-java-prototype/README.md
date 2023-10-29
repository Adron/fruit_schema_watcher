A few notes about operation.

The server should run in a production WSGI server, so I generally run that with gunicorn. The install I used for that is:

`pip install Flask Flask-GraphQL graphene gunicorn`

