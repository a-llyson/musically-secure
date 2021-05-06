from password import password_gen, note_password_gen, convert_all 
from music import play_password
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
