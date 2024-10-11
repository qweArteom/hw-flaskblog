from flask import Blueprint, render_template, request

from app.db import Session, User, Post
from app.data.password import ADMIN_PASS


post_route = Blueprint("posts", __name__)


@post_route.get("/posts/")
@post_route.post("/posts/")
def add_post():
    msg = ""
    block = False

    with Session() as session:
        if request.method == "POST":
            title = request.form.get("title")
            text = request.form.get("text")
            user_id = request.form.get("user_id")

            if request.form.get("password") == ADMIN_PASS:
                post = Post(title=title, text=text, user_id=user_id)
                session.add(post)
                session.commit()
                msg = "Статтю успішно додано"
            else:
                block = True

        users = session.query(User).all()
        context = {
            "msg": msg,
            "block": block,
            "users": users
        }
        return render_template("add_post.html", **context)


@post_route.get("/")
def index():
    with Session() as session:
        posts = session.query(Post).all()
        return render_template("index.html", posts=posts)


@post_route.get("/post/<int:id>")
def get_post(id):
    with Session() as session:
        post = session.query(Post).where(Post.id == id).first()
        return render_template("post.html", post=post)
