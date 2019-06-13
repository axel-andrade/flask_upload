import os
import sqlite3
import upload

from flask import Flask, render_template, request

app = Flask(__name__)

wsgi_app = app.wsgi_app

@app.route('/', methods=["GET", "POST"])
def hello():
    return "Hello World"

@app.route('/upload', methods=["GET", "POST"])
def upload_file():
    if request.method=="POST":
        file = request.files["file"]
        file.save(os.path.join("uploads", file.filename))
        upload.createUpload(file.filename, request.form["username"])
        return render_template("index.html", message="success")
    return render_template("index.html", message="Upload")

@app.route('/uploads', methods=["GET", "POST"])
def getUploads():
    return upload.getUploads()


if __name__ == '__main__':
    app.run(debug=True)