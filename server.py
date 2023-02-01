from flask import Flask, render_template, request, redirect, url_for
from audio_to_freq import getNotes
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route('/')
def index():
    print("entering index");
    return render_template('index.html')

@app.route('/transcribed/', methods = ['GET', 'POST'])
def write_notes():
    print("ENTERING WRITE_NOTES")
    print(request.files)
    file = request.files['file'];
    filename = secure_filename(file.filename)
    file.save(os.path.join('audios', filename))
    notes = getNotes('')
    print(notes)
    return render_template('transcribed.html', notes = notes)

if __name__ == '__main__':
    app.run(debug=True)