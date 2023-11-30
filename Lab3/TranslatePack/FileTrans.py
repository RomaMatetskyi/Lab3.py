
from deep_translator import GoogleTranslator as Translator
from langdetect import DetectorFactory, detect
import json
import os
import re
DetectorFactory.seed = 0

def count_sentences(text):
    sentence_pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s'
    sentences = re.split(sentence_pattern, text)
    return len(sentences)
def load_config(file_path):
    with open(file_path, 'r') as config_file:
        return json.load(config_file)

def main():
    config = load_config('config.json')

    if not os.path.exists(config['input_file']):
        print("Помилка: Вхідний файл не існує.")
    else:
        with open(config['input_file'], 'r', encoding='utf-8') as input_file:
            input_text = input_file.read()

        source_language = detect(input_text)

        num_characters = len(input_text)
        num_words = len(input_text.split())
        num_sentences = count_sentences(input_text)

        print("Назва файлу:", config['input_file'])
        print("Розмір файлу:", os.path.getsize(config['input_file']), "байт")
        print("Кількість символів:", num_characters)
        print("Кількість слів:", num_words)
        print("Кількість речень:", num_sentences)
        print("Мова тексту:", source_language)

        if (num_characters > config['max_characters'] or
            num_words > config['max_words'] or
            num_sentences > config['max_sentences']):
            print("Обмеження на кількість символів, слів або речень перевищені.")
        else:
            try:
                translated_text = Translator(source=source_language, target=config['target_language']).translate(input_text)

                if config['output_mode'] == 'file':
                    output_filename = f"output_{config['target_language']}.txt"
                    with open(output_filename, 'w', encoding='utf-8') as output_file:
                        output_file.write(f"Мова перекладу: {config['target_language']}\n")
                        output_file.write(translated_text)
                    print(f"Результат збережено у файлі {output_filename}")
                elif config['output_mode'] == 'screen':
                    print(f"Мова перекладу: {config['target_language']}")
                    print(translated_text)
                else:
                    print("Помилка: Невірний режим виведення результату.")

            except Exception as e:
                print(f"Помилка під час перекладу: {str(e)}")

if __name__ == "__main__":
    main()
