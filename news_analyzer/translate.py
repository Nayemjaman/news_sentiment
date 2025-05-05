from googletrans import Translator

def translate_to_english(text):
    translator = Translator()
    result = translator.translate(text, src='bn', dest='en')
    return result.text