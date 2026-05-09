from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    translated_text = ""
    input_text = ""
    source_lang = "en" 
    target_lang = "it" 

    if request.method == 'POST':
        # Get the data from the HTML form
        input_text = request.form.get('input_text', '')
        source_lang = request.form.get('source_lang', 'en')
        target_lang = request.form.get('target_lang', 'it')

        if input_text:
            try:
                translator = GoogleTranslator(source=source_lang, target=target_lang)
                translated_text = translator.translate(input_text)
            except Exception as e:
                translated_text = f"Error: {e}"

    return render_template('index.html', 
                           translated_text=translated_text, 
                           input_text=input_text,
                           source_lang=source_lang,
                           target_lang=target_lang)

if __name__ == '__main__':
    app.run(debug=True)