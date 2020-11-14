import requests
from bs4 import BeautifulSoup
import logging

logger = logging.basicConfig(level=logging.INFO)


def get_URL(language_from, language_to, word):
    return f'https://context.reverso.net/translation/{language_from.lower()}-{language_to.lower()}/{word}'


def check_HTTP_status(r):
    if r.status_code == 200:
        print("200 OK")
        return True
    else:
        return False


def choose_language():
    language_dict = {
        1: "Arabic",
        2: "German",
        3: "English",
        4: "Spanish",
        5: "French",
        6: "Hebrew",
        7: "Japanese",
        8: "Dutch",
        9: "Polish",
        10: "Portuguese",
        11: "Romanian",
        12: "Russian",
        13: "Turkish",
    }
    print("Hello, you're welcome to the translator. Translator supports:\n"
          "1. Arabic\n"
          "2. German\n"
          "3. English\n"
          "4. Spanish\n"
          "5. French\n"
          "6. Hebrew\n"
          "7. Japanese\n"
          "8. Dutch\n"
          "9. Polish\n"
          "10. Portuguese\n"
          "11. Romanian\n"
          "12. Russian\n"
          "13. Turkish\n")
    language_from = int(input("Type the number of your language:\n"))
    language_to = int(input("Type the number of language you want to translate to:\n"))
    return language_dict[language_from], language_dict[language_to]


def chose_word_to_translate():
    words = input('Type the word you want to translate:')
    return words


def translate_words(r):
    soup = BeautifulSoup(r.content, 'html.parser')
    translations = soup \
        .find('div', id="translations-content") \
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
    translations = soup \
        .find('section', id="examples-content") \
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
    language_from, language_to = choose_language()
    word = chose_word_to_translate()
    # word = 'cheese'
    url = get_URL(language_from, language_to, word)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"}
    logging.debug(f"url: {url}")
    r = requests.get(url, headers=headers)

    if check_HTTP_status(r):
        translated_words = translate_words(r)
        translated_sentences = translate_sentences(r)
        print(f"\n{language_to} Translations:")
        print_translated_words(translated_words)
        print(f"\n{language_to} Examples:")
        print_translated_sentences(translated_sentences)
        logging.debug(len(translated_words))


if __name__ == "__main__":
    main()
