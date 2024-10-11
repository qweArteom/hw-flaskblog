from flask import Flask

from app.db import create_db
from app.routes import position_route, user_route, post_route


app = Flask(__name__)
app.register_blueprint(position_route)
app.register_blueprint(user_route)
app.register_blueprint(post_route)


def main():
    create_db()
    app.run(debug=True)
