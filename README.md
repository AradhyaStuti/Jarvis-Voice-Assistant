
# 🎙️ Jarvis – Python Voice Assistant

A desktop-based voice assistant built with Python that listens for the wake word **“Jarvis”** and executes commands such as opening websites, playing YouTube songs, and reading top news headlines.

---

## 🚀 Features

* 🎤 Wake word detection (“Jarvis”)
* 🔊 Natural text-to-speech responses
* 🌐 Open popular websites:

  * Google
  * Facebook
  * Instagram
  * LinkedIn
* 🎵 Play songs directly from YouTube
* 📰 Fetch and read top US headlines using NewsAPI
* 🧵 Thread-safe speech execution
* 🎯 Continuous listening mode

---

## 🛠️ Tech Stack

| Technology         | Purpose                   |
| ------------------ | ------------------------- |
| Python             | Core programming language |
| speech_recognition | Voice input recognition   |
| pyttsx3            | Text-to-speech engine     |
| requests           | API calls                 |
| webbrowser         | Open websites             |
| threading          | Safe speech execution     |
| NewsAPI            | Fetch live news           |

---

## 📂 Project Structure

```
jarvis-voice-assistant/
│
├── main.py
├── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/AradhyaStuti/Jarvis-Voice-Assistant.git
cd jarvis-voice-assistant
```

### 2️⃣ Install Dependencies

```bash
pip install speechrecognition pyttsx3 requests pyaudio
```

> ⚠ If `pyaudio` fails on Windows, install a compatible wheel file.

---

## 🔑 API Configuration

This project uses **NewsAPI**.

1. Create a free account at
   [https://newsapi.org](https://newsapi.org)

2. Replace the API key in your script:

```python
newsapi_key = "YOUR_API_KEY"
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 🗣️ Usage Guide

1. Say **“Jarvis”**
2. Wait for response: **“Ya”**
3. Give your command

### Example Commands

* “Open Google”
* “Open Instagram”
* “Play Believer”
* “Tell me the news”

---

## 🔍 How It Works

* Continuously listens using microphone input.
* Detects wake word before processing commands.
* Uses Google Speech Recognition for speech-to-text.
* Executes conditional command logic.
* Fetches news via HTTP request.
* Extracts first YouTube video ID from search results.
* Uses thread-based speech output to prevent blocking.

---

## 📌 Requirements

* Python 3.x
* Working microphone
* Internet connection

---

## 📈 Future Improvements (Optional Section for Profile Strength)

* GUI Interface
* Custom wake word
* System control commands
* Spotify integration
* Weather API integration

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Your Name**
GitHub: [https://github.com/AradhyaStuti]

---



