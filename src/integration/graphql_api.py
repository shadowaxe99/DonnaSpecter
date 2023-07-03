```python
from flask import Flask
from flask_graphql import GraphQLView
from graphene import ObjectType, String, Schema

class Query(ObjectType):
    hello = String(name=String(default_value="World"))
    user_email = String()
    user_credentials = String()

    def resolve_hello(self, info, name):
        return f'Hello {name}!'

    def resolve_user_email(self, info):
        return USER_EMAIL

    def resolve_user_credentials(self, info):
        return USER_CREDENTIALS

schema = Schema(query=Query)

app = Flask(__name__)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run()
```