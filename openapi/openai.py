import openai
from flask import Flask

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

openai.api_key = app.config['OPENAI_API_KEY']


def generate_text(text):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=text,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5
        )

        return response.choices[0].text.strip()
    except openai.error.RateLimitError as e:
        print(f"OpenAI API request exceeded rate limit: {e}")
        pass

