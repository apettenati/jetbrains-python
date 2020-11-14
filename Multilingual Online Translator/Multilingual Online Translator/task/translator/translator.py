import requests
from bs4 import BeautifulSoup
import logging


logger = logging.basicConfig(level=logging.INFO)


def get_URL(language, word):
    if language == 'fr':
        return f'https://context.reverso.net/translation/english-french/{word}'
    if language == 'en':
        return f'https://context.reverso.net/translation/french-english/{word}'


def check_HTTP_status(r):
    if r.status_code == 200:
        print("200 OK")
        return True
    else:
        return False

def choose_language():
    language = input('Type "en" if you want to translate from French into English,'
                     'or "fr" if you want to translate from English into French:')
    return language


def chose_word_to_translate():
    words = input('Type the word you want to translate:')
    return words

def translate_words(r):
    soup = BeautifulSoup(r.content, 'html.parser')
    translations = soup\
        .find('div', id="translations-content")\
        .find_all('a', {"class": "translation"})
    # logging.debug(translations)
    translated_words = []
    for word in translations:
        # logging.debug(word)
        translated_words.append(word.text.replace('\n', '').strip())
    return translated_words[0:5]

def print_translated_words(translated_words):
    for word in translated_words:
        print(word)

def translate_sentences(r):
    soup = BeautifulSoup(r.content, 'html.parser')
    translations = soup\
        .find('section', id="examples-content")\
        .find_all('span', {"class": "text"})
    logging.debug(translations)
    translated_sentences = []
    for sentence in translations:
        logging.debug(sentence.text)
        translated_sentences.append(sentence.text.replace('\n', '').strip())
    return translated_sentences[0:10]

def print_translated_sentences(translated_stentences):
    tracker = False
    for sentence in translated_stentences:
        print(sentence)
        if tracker:
            print()
        tracker = not tracker


def main():
    language_dict = {'fr':'French', 'en': 'English'}
    language = choose_language()
    word = chose_word_to_translate()
    # language = 'fr'
    # word = 'cheese'
    print(f'You chose "{language}" as the language to translate "{word}" to.')
    url = get_URL(language, word)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"}
    logging.debug(f"url: {url}")
    r = requests.get(url, headers=headers)

    if check_HTTP_status(r):
        translated_words = translate_words(r)
        translated_sentences = translate_sentences(r)
        print(f"\nContext Examples:\n"
              f"\n{language_dict[language]} Translations:")

        print_translated_words(translated_words)
        print(f"\n{language_dict[language]} Examples:")
        print_translated_sentences(translated_sentences)
        logging.debug(len(translated_words))

    else:
        print("Connection failed")

if __name__ == "__main__":
    main()
