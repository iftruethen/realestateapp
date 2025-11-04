import math, time, markupsafe
from flask import Flask
from flask import abort, flash
from flask import redirect, render_template, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
import config#, lists, userlogic, secrets
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
app.secret_key = config.secret_key
app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
db = SQLAlchemy(app)

def require_login():
    if "user_id" not in session:
        abort(403)

def check_csrf():
    if request.form["csrf_token"] != session["csrf_token"]:
        abort(403)

@app.route("/")
def index():
    creation_sql = """
        CREATE TABLE realestates (
        id SERIAL PRIMARY KEY,
        osoite TEXT,
        hinta TEXT,
        kaupunki TEXT,
        makuuhuoneita TEXT,
        pintaala TEXT,
        user_id INTEGER REFERENCES users
        );
    """
    db.session.execute(text(creation_sql))
    db.session.execute(text("INSERT INTO realestates (osoite) VALUES ('foobarkatu 1')"))
    result = db.session.execute(text("SELECT osoite FROM realestates"))
    messages = result.fetchall()
    return render_template("index.html", osoitteet = messages)