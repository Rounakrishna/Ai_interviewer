from flask import Flask, render_template, request, jsonify
import win32com.client
import webbrowser
import speech_recognition as sr

speaker = win32com.client.Dispatch("SAPI.SpVoice")
app = Flask(__name__)

def say(text):
    speaker.speak(text)

@app.route('/')
def index():
    return render_template('index.html', result="")

@app.route('/start_interview', methods=['POST'])
def start_interview():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            audio = r.listen(source)
            query = r.recognize_google(audio, language="en-in")
            result = {"result": query}
            print(result)
            return render_template('index.html', result=result)
    except Exception as e:
        error_message = "Some Error Occurred. Sorry from Jarvis"
        return render_template('index.html', result="", error=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
