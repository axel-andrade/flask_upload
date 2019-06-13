import os
import upload
from flask import Flask, render_template, request, send_from_directory, send_file

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
def uploads():
    uploads = upload.getUploads();
    print("tamanho: ", len(uploads))
    return render_template("listUploads.html", uploads=uploads, deleteUpload=upload.deleteUpload)

@app.route('/delete/<int:id>')
def delete_upload(id):
    upload.deleteUpload(id)
    uploads = upload.getUploads();
    print("tamanho: ", len(uploads))
    return render_template("listUploads.html", uploads=uploads)

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    path = "uploads/"+filename
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)