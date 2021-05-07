from password import password_gen, note_password_gen, convert_all 
from music import play_password
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        number = request.form["number"]
        length = request.form["length"]
        list_of_passwords = password_gen(int(number), int(length))
        list_of_notes = convert_all(note_password_gen(list_of_passwords))
        file_names = play_password(list_of_notes)
        return render_template("sound.html", passwords_sounds=zip(list_of_passwords, file_names))
    else:
        return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
