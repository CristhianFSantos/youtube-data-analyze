from googletrans import LANGUAGES, Translator

class TranslateTools:

    def detect_language(self, text):
        translator = Translator()
        detected_lang = translator.detect(text).lang
        lang_name = LANGUAGES.get(detected_lang).title()
        return lang_name

    def translate_text(self, text, dest_lang='en'):
        translator = Translator()
        translated = translator.translate(text, dest=dest_lang)
        return translated.text