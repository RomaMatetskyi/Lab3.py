from googletrans import Translator

translator = Translator()

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
        "zh-cn": "Chinese (Simplified)",
        "zh-tw": "Chinese (Traditional)",
        "nl": "Dutch",
        "el": "Greek",
        "he": "Hebrew",
        "hi": "Hindi",
        "tr": "Turkish",
        "uk": "Ukrainian"
    }


def GoogleTranslate(text: str, src: str, dest: str) -> str:
    try:
        translated_text = translator.translate(text, src=src, dest=dest).text
        return translated_text
    except Exception as e:
        return str(e)

def DetectLanguage(text: str, set: str = "all") -> str:
    try:
        detected = translator.detect(text)
        if detected:
            if set == "lang":
                return detected.lang
            elif set == "confidence":
                return str(detected.confidence)
            else:
                return f"Мова: {detected.lang}, Точність: {detected.confidence}"
        else:
            return "Не вдалося визначити мову"
    except Exception as e:
        return str(e)


def LanguageCode(lang: str) -> str:

    if lang in LANGUAGES:
        return LANGUAGES[lang]
    else:
        for code, name in LANGUAGES.items():
            if name == lang:
                return code
        return "Мова не знайдена"

def LanguageList(out: str = "screen", text: str = None) -> str:
    try:
        if out == "screen":
            print("N\tLanguage\tISO-639 code\tText")
            print("-" * 40)
            for i, (code, lang) in enumerate(LANGUAGES.items(), start=1):
                if text:
                    translation = GoogleTranslate(text, 'auto', code)
                    print(f"{i}\t{lang}\t{code}\t{translation}")
                else:
                    print(f"{i}\t{lang}\t{code}\t")
            return "Ok"
        elif out == "file":
            filename = "GoogleFile.txt"
            with open(filename, "w", encoding="utf-8") as file:
                file.write("N\tLanguage\tISO-639 code\tText\n")
                file.write("-" * 40 + "\n")
                for i, (code, lang) in enumerate(LANGUAGES.items(), start=1):
                    if text:
                        translation = GoogleTranslate(text, 'auto', code)
                        file.write(f"{i}\t{lang}\t{code}\t{translation}\n")
                    else:
                        file.write(f"{i}\t{lang}\t{code}\t\n")
            return f"Збережено в: {filename}"
        else:
            return "Помилка 'out'"
    except Exception as e:
        return str(e)