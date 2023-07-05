```python
from google.cloud import texttospeech

def synthesize_speech(text, language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL):
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code, ssml_gender=ssml_gender
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )

    return response.audio_content

def save_speech(audio_content, filename):
    with open(filename, "wb") as out:
        out.write(audio_content)
        print(f'Audio content written to file "{filename}"')

def generate_speech_from_text(text, filename):
    audio_content = synthesize_speech(text)
    save_speech(audio_content, filename)
```
This Python script uses Google's Text-to-Speech API to convert text into speech. The `synthesize_speech` function takes in a string of text and optional parameters for language and gender of the voice, and returns the audio content. The `save_speech` function takes this audio content and a filename, and writes the audio content to a file with the given name. The `generate_speech_from_text` function combines these two functions to generate speech from a given text and save it to a file.