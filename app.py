from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import subprocess
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():

    file = request.files["video"]

    filename = str(uuid.uuid4()) + ".mp4"
    video_path = os.path.join(UPLOAD_FOLDER, filename)

    file.save(video_path)

    mp3_name = filename.replace(".mp4", ".mp3")
    mp3_path = os.path.join(OUTPUT_FOLDER, mp3_name)

    subprocess.run([
        "ffmpeg",
        "-i", video_path,
        "-q:a", "0",
        "-map", "a",
        mp3_path
    ])

    return jsonify({"file": mp3_name})


@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(OUTPUT_FOLDER, filename, as_attachment=True)


@app.route("/play/<filename>")
def play(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)


if __name__ == "__main__":
    app.run(debug=True)