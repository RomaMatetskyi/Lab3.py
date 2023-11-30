from deep_translator import GoogleTranslator as Translator
from langdetect import detect

LANGUAGES = {
        "en": "English",
        "fr": "French",
        "es": "Spanish",
        "af": "Afrikaans",
        "bg": "Bulgarian",
        "ar": "Arabic",
        "de": "German",
        "it": "Italian",
        "ja": "Japanese",
        "ko": "Korean",
        "pt": "Portuguese",
        "ru": "Russian",
        "nl": "Dutch",
        "el": "Greek",
        "he": "Hebrew",
        "hi": "Hindi",
        "tr": "Turkish",
        "uk": "Ukrainian"
    }

def translate_text(text: str, source_lang: str, target_lang: str) -> str:
    try:
        translated_text = Translator(source=source_lang, target=target_lang).translate(text)
        return translated_text
    except Exception as e:
        return str(e)

def detect_language(text: str, return_type: str = "language") -> str:
    try:
        detected_lang = detect(text)
        if return_type == "language":
            return detected_lang
        elif return_type == "confidence":
            return "Не підтримується"
        else:
            return f"Language: {detected_lang}, Confidence: Не підртимується"
    except Exception as e:
        return str(e)

def language_code_to_name(language_code: str) -> str:
    if language_code in LANGUAGES:
        return LANGUAGES[language_code]
    else:
        for code, name in LANGUAGES.items():
            if name == language_code:
                return code
        return "Мова не знайдена"

def list_languages(output_type: str = "screen", text: str = None) -> str:
    try:
        if output_type == "screen":
            print("N\tLanguage\tISO-639 code\tText")
            print("-" * 40)
            for i, (code, lang) in enumerate(LANGUAGES.items(), start=1):
                if text:
                    translation = translate_text(text, 'auto', code)
                    print(f"{i}\t{lang}\t{code}\t{translation}")
                else:
                    print(f"{i}\t{lang}\t{code}\t")
            return "Ok"
        elif output_type == "file":
            filename = "DeepFile.txt"
            with open(filename, "w", encoding="utf-8") as file:
                file.write("N\tLanguage\tISO-639 code\tText\n")
                file.write("-" * 40 + "\n")
                for i, (code, lang) in enumerate(LANGUAGES.items(), start=1):
                    if text:
                        translation = translate_text(text, 'auto', code)
                        file.write(f"{i}\t{lang}\t{code}\t{translation}\n")
                    else:
                        file.write(f"{i}\t{lang}\t{code}\t\n")
            return f"Збережено в: {filename}"
        else:
            return "Помилка 'output_type'"
    except Exception as e:
        return str(e)