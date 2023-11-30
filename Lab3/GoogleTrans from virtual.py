from TranslatePack.GoogleTranslate import GoogleTranslate, LanguageCode, DetectLanguage, LanguageList

def main():
    translated_text = GoogleTranslate("Hallo", src="de", dest="uk")
    print("\tGoogleTranslate")
    print(translated_text)

    print("\n\tDetectLanguage")
    text = "Hello"
    lang = DetectLanguage(text, set="lang")
    confidence = DetectLanguage(text, set="confidence")
    print("Мова тексту:", lang)
    print("Точність визначення мови:", confidence)

    print("\n\tLanguageCode")
    language_name = "English"
    language_code = "tr"

    code_from_name = LanguageCode(language_name)
    name_from_code = LanguageCode(language_code)

    print(f"Код мови '{language_name}': {code_from_name}")
    print(f"Назва мови '{language_code}': {name_from_code}")

    print("\n\tLanguageList")
    LanguageList("file", "Добрий день")

if __name__ == "__main__":
    main()
