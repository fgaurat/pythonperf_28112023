from flask import Flask,render_template
from UserDAO import UserDAO
app = Flask(__name__)

# flask run

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/users_old")
def users_old():
    dao = UserDAO('users_db.db')
    users = dao.findAll()
    html=""
    for user in users:
        html+=f"""
        <tr>
            <td>{user.id}</td>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.email}</td>
        </tr>
        """
    
    return f"<table>{html}</table>"

@app.route("/users")
def users():
    dao = UserDAO('users_db.db')
    users = dao.findAll()
    return render_template("users.html",users=users)