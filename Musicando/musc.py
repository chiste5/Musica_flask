import os, sys
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask import Flask, render_template,request


app = Flask(__name__, template_folder=os.path.abspath("templates"))



@app.route('/', methods=('GET', 'POST'))
def index():
    music = request.form.get("mus","Bem-Vindo ao Play Back")
    musica = str(music) +".mp3"
    img = str(music)+".png"

    return render_template("home.html",music=musica,image_name=img,nome=music)

if __name__ == "__main__":
    app.run(debug=True)
