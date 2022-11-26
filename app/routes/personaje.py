from flask import Blueprint, render_template, flash, redirect, url_for
from app.forms import BookForm
from app.models.book import Book
from app.db import db 

personaje = Blueprint("personaje", __name__)

@personaje.route("/")
def index():
  personajes = db.character.find().sort('name',-1)

  return render_template("index.html",personajes=personajes)

@personaje.route('/character/<id>')
def get_character(id):
  
  p=db.character.find_one({'id':int(id)})
  print(p)

  return render_template('personaje.html',personaje=p)