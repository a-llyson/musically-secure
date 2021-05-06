from password import password_gen, note_password_gen, convert_all 
from music import play_password
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        print("hl")
        number = request.form["name"]
        length = request.form["length"]
        list_of_passwords = password_gen(number, length)
        list_of_notes = convert_all(note_password_gen(list_of_passwords))
        return render_template("sound.html", list_of_passwords=list_of_passwords, length=length)
    else:
        return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
