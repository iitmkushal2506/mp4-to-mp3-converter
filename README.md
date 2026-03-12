# 🎧 Kush's MP4 to MP3 Converter

A modern web-based tool that converts **MP4 video files into MP3 audio files** quickly and easily.

Users can upload a locally stored MP4 video, convert it into MP3 format, preview the audio directly in the browser, and download the converted file.

The project features a **clean Spotify-inspired interface**, a **Flask backend**, and **FFmpeg-powered audio extraction**.

---

## 🌐 Live Demo

https://mp4-to-mp3-converter-ai0t.onrender.com

---

## ✨ Features

* Convert **MP4 videos to MP3 audio**
* **Play audio in-browser** before downloading
* Clean **Spotify-inspired dark UI**
* Fast server-side audio extraction using **FFmpeg**
* Simple and intuitive interface
* Fully deployed **web application**
* Automatic deployment from GitHub

---

## ⚠️ Important Note

This application **is NOT a YouTube downloader or streaming converter**.

It only works with **MP4 files that are already downloaded on your device**.

Users must upload a locally stored video file to convert it.

---

## 🛠 Technologies Used

### Backend

* Python
* Flask Web Framework
* FFmpeg (Audio Extraction)
* Gunicorn Production Server

### Frontend

* HTML
* CSS
* JavaScript

### Deployment

* Render (Cloud Hosting)
* GitHub (Source Code Hosting)

---

## ⚙️ How the Conversion Works

1. The user uploads an **MP4 video file** through the web interface.
2. The file is sent to the **Flask backend server**.
3. The server temporarily stores the uploaded video.
4. A **Python subprocess command runs FFmpeg**.
5. FFmpeg extracts the audio stream from the video.
6. The audio is converted into **MP3 format**.
7. The resulting MP3 file is sent back to the browser.
8. The user can **play the audio or download it**.

---

## 📂 Project Structure

```
mp4-to-mp3-converter
│
├── app.py                # Flask backend server
├── requirements.txt      # Python dependencies
│
├── templates
│   └── index.html        # Website layout
│
├── static
│   └── style.css         # Styling and UI
│
└── README.md
```

---

## 🚀 Running the Project Locally

### 1️⃣ Clone the repository

```
git clone https://github.com/iitmkushal2506/mp4-to-mp3-converter.git
cd mp4-to-mp3-converter
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Install FFmpeg

Download FFmpeg from:

https://ffmpeg.org/download.html

Make sure **FFmpeg is added to your system PATH**.

### 4️⃣ Run the server

```
python app.py
```

Open in your browser:

```
http://127.0.0.1:5000
```

---

## ☁️ Deployment

This application is deployed using **Render**.

Deployment workflow:

1. Code is pushed to **GitHub**
2. Render automatically detects the new commit
3. The application is rebuilt
4. The updated version is deployed online

---

## 👨‍💻 Author

**Kushal Batra**

Student — **BS in Data Science and Applications (IIT Madras)**

GitHub Profile:
https://github.com/iitmkushal2506

Project Repository:
https://github.com/iitmkushal2506/mp4-to-mp3-converter

---

## 📜 License

This project is open-source and intended for **learning and educational purposes**.
