from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route("/post/<int:number>")
def post_page(number):
    return render_template("post.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/admin")
def login():
    return render_template("admin.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/new_post")
def create_post():
    return render_template("create_post.html")

if __name__ == "__main__":
    app.run(debug=True)