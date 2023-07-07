```python
import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        text = r.recognize_google(audio, language='en-US')
        print(f"User said: {text}\n")
        return text

    except Exception as e:
        print("Could not understand audio, please try again.")
        return None
```