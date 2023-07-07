```python
from gtts import gTTS
import os

class TextToSpeech:
    def __init__(self):
        pass

    def convert_text_to_speech(self, text, language='en'):
        speech = gTTS(text = text, lang = language, slow = False)
        speech.save("Ely_Speech.mp3")

    def play_speech(self):
        os.system("mpg321 Ely_Speech.mp3")

if __name__ == "__main__":
    tts = TextToSpeech()
    tts.convert_text_to_speech("Hello, I am Ely, your holographic assistant.")
    tts.play_speech()
```