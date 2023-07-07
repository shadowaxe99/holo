```python
import GPT3_Interface
import Speech_to_Text
import Text_to_Speech
import Database_Connection

class Backend_Communication:
    def __init__(self):
        self.gpt3_interface = GPT3_Interface.GPT3_Interface()
        self.speech_to_text = Speech_to_Text.Speech_to_Text()
        self.text_to_speech = Text_to_Speech.Text_to_Speech()
        self.database_connection = Database_Connection.Database_Connection()

    def process_voice_input(self, voice_input):
        text_input = self.speech_to_text.convert(voice_input)
        response = self.gpt3_interface.generate_response(text_input)
        self.database_connection.store_interaction(text_input, response)
        voice_output = self.text_to_speech.convert(response)
        return voice_output

    def process_text_input(self, text_input):
        response = self.gpt3_interface.generate_response(text_input)
        self.database_connection.store_interaction(text_input, response)
        return response
```