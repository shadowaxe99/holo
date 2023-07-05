```python
import os
from google.cloud import speech_v1p1beta1 as speech

def transcribe_audio(audio_file_path):
    client = speech.SpeechClient()

    with open(audio_file_path, "rb") as audio_file:
        input_audio = audio_file.read()

    audio = speech.RecognitionAudio(content=input_audio)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))

    return response

def main():
    audio_file_path = "path_to_your_audio_file"
    transcribe_audio(audio_file_path)

if __name__ == "__main__":
    main()
```
This script uses Google's Speech-to-Text API to transcribe audio from a given file. The `transcribe_audio` function opens the audio file, reads its content, and sends it to the API for transcription. The transcribed text is then printed to the console. The `main` function is where you should specify the path to your audio file.