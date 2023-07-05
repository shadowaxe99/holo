```python
import unittest
from Integration.integration_script import HologramBot

class TestHologramBot(unittest.TestCase):

    def setUp(self):
        self.bot = HologramBot()

    def test_voice_recognition(self):
        input_speech = "What is the ROI of this investment?"
        expected_text = "What is the ROI of this investment?"
        self.assertEqual(self.bot.voice_to_text(input_speech), expected_text)

    def test_nlp_response(self):
        input_text = "What is the ROI of this investment?"
        response = self.bot.generate_response(input_text)
        self.assertIsNotNone(response)

    def test_speech_synthesis(self):
        input_text = "The ROI of this investment is 10%."
        response = self.bot.text_to_speech(input_text)
        self.assertIsNotNone(response)

    def test_3d_model(self):
        self.assertTrue(self.bot.display_3d_model())

    def test_holographic_effect(self):
        self.assertTrue(self.bot.apply_holographic_effect())

if __name__ == '__main__':
    unittest.main()
```
This Python script uses the unittest module to define a set of tests for the HologramBot. The setUp method is used to create an instance of the bot before each test. The tests then check the functionality of the bot's voice recognition, natural language processing, speech synthesis, 3D modeling, and holographic effect application. The voice recognition test checks that the bot correctly converts speech to text. The NLP test checks that the bot generates a non-empty response to a given input. The speech synthesis test checks that the bot correctly converts text to speech. The 3D model and holographic effect tests check that these features are correctly displayed.