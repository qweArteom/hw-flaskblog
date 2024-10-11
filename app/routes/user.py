from flask import Blueprint, render_template, request

from app.db import Session, User, Position
from app.data.password import ADMIN_PASS

user_route = Blueprint("users", __name__, url_prefix="/users/")


@user_route.get("/")
@user_route.post("/")
def add_user():
    msg = ""
    block = False

    with Session() as session:
        if request.method == "POST":
            first_name = request.form.get("first_name")
            last_name = request.form.get("last_name")
            age = request.form.get("age")
            position_id = request.form.get("position_id")
            user = User(first_name=first_name, last_name=last_name, age=age, position_id=position_id)

            if request.form.get("password") == ADMIN_PASS:
                session.add(user)
                session.commit()
                msg = "Користувача успішно додано"
            else:
                block = True

        positions = session.query(Position).all()
        context = {
            "msg": msg,
            "block": block,
            "positions": positions
        }

        return render_template("add_user.html", **context)
