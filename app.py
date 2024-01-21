from flask import Flask, render_template, request
from googletrans import Translator
from gtts import gTTS
from gtts.langs import _main_langs
# import time
import random
# import asyncio
# import os

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['GET','POST'])
async def translate():
    text_to_translate = request.form['input_text']
    target_language = request.form['target_language']

    translation = translator.translate(text_to_translate, dest=target_language)
    translated_text = translation.text

    langs = dict()
    langs.update(_main_langs())
    lang = (list(langs.keys())[list(langs.values()).index(target_language.capitalize())])

    tts = gTTS(text=translated_text, lang=lang, slow=False)
    # os.system("python_prac/static/output.wav")
    # await asyncio.sleep(2)
    
    # timestamp = int(time.time())
    random_param = random.randint(1, 10)
    audio_file_url = f'output_{random_param}.wav'
    tts.save(f'python_prac/static/{audio_file_url}')
    return render_template('index.html', translated_text=translated_text, input_text=text_to_translate, audio_file=audio_file_url)

if __name__ == '__main__':
    app.run(debug=True)
