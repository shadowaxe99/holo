```python
import openai

openai.api_key = 'your-api-key'

class GPT3_Interface:
    def __init__(self):
        self.model = "text-davinci-003"  # GPT-3.5 model

    def process(self, prompt, max_tokens=100):
        response = openai.Completion.create(
            engine=self.model,
            prompt=prompt,
            max_tokens=max_tokens
        )
        return response.choices[0].text.strip()

gpt3_interface = GPT3_Interface()
```