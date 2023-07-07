from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@localhost/flask_blog"
app.config['SECRET_KEY'] = "thesecretkeywhichissupposedtobesecret"
db = SQLAlchemy(app)
admin = Admin(app)

# DATABASE CLASS
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    content = db.Column(db.Text)
    date = db.Column(db.DateTime)
    slug = db.Column(db.String(255))

with app.app_context():
    db.create_all()

admin.add_view(ModelView(Posts, db.session))

@app.route("/")
def homepage():
    posts = Posts.query.all()
    return render_template("homepage.html", posts=posts)

@app.route("/post/<string:slug>")
def post_page(slug):
    try:
        post = Posts.query.filter_by(slug=slug).one()
        return render_template("post.html", post=post)
    except:
        abort(404)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)