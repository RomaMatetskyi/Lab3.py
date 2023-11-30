from TranslatePack.DeepTranslate import translate_text, detect_language, language_code_to_name,list_languages

def main():
    print("\n\tTranslate_text")
    translated_text = translate_text("Hallo!", source_lang="de", target_lang="uk")
    print(translated_text)

    print("\n\tDetect_language")
    text = "Привіт"
    lang = detect_language(text, return_type="language")
    confidence = detect_language(text, return_type="confidence")

    print("Мова:", lang)
    print("Точність:", confidence)


    print("\n\tLanguage_code_to_name")
    language_name = "Bulgarian"
    language_code = "de"

    translated_name = language_code_to_name(language_name)
    translated_code = language_code_to_name(language_code)

    print(f"Переклад назви мови '{language_name}': {translated_name}")
    print(f"Переклад коду мови '{language_code}': {translated_code}")

    print("\n\tList_languages")
    result = list_languages("file", "Hello")
    print(result)

if __name__ == "__main__":
    main()
