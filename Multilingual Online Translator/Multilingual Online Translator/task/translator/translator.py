import requests
from bs4 import BeautifulSoup
import logging
import sys

logging.basicConfig(level=logging.DEBUG)

available_languages = [
        "arabic",
        "german",
        "english",
        "spanish",
        "french",
        "hebrew",
        "japanese",
        "dutch",
        "polish",
        "portuguese",
        "romanian",
        "russian",
        "turkish",
    ]
unavailable_languages = ["korean"]

def get_URL(language_from, language_to, word):
    url = f'https://context.reverso.net/translation/{language_from}-{language_to}/{word}'
    logging.debug(f"url: {url}")
    return url


def check_HTTP_status(request):
    if request.status_code == 200:
        return True
    else:
        print("Something wrong with your internet connection")
        return False


def create_request(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"}
    request = requests.get(url, headers=headers)
    return request


def choose_language():
    language_dict = {
        0: "all",
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
    language_to = int(input("Type the number of language you want to translate to "
                            "or '0' to translate all languages:\n"))
    return language_dict[language_from], language_dict[language_to]


def chose_word_to_translate():
    word = input('Type the word you want to translate:')
    return word


def translate_words(request):
    soup = BeautifulSoup(request.content, 'html.parser')
    translations = soup \
        .find('div', id="translations-content") \
        .find_all('a', {"class": "translation"})
    # logging.debug(translations)
    translated_words = []
    for word in translations:
        # logging.debug(word)
        translated_words.append(word.text.replace('\n', '').strip())
    return translated_words[0:5]


def print_translated_words(language_to, translated_words):
    all_translated_words = f'{language_to} Translations:\n'
    for word in translated_words:
        all_translated_words += f"{word}\n"
    return all_translated_words


def translate_sentences(request):
    soup = BeautifulSoup(request.content, 'html.parser')
    translations = soup \
        .find('section', id="examples-content") \
        .find_all('span', {"class": "text"})
    # logging.debug(translations)
    translated_sentences = []
    for sentence in translations:
        # logging.debug(sentence.text)
        translated_sentences.append(sentence.text.replace('\n', '').strip())
    return translated_sentences[0:10]


def print_translated_sentences(language_to, translated_sentences):
    all_translated_sentences = f'{language_to} Examples: \n'
    tracker = False
    for sentence in translated_sentences:
        all_translated_sentences += f'{sentence}\n'
        if tracker:
            all_translated_sentences += '\n'
        tracker = not tracker
    return all_translated_sentences


def translate_all_languages(language_from, word):
    remaining_languages = [x for x in available_languages if x != language_from]
    for language_to in remaining_languages:
        url = get_URL(language_from, language_to, word)
        request = create_request(url)
        translated_words = translate_words(request)
        translated_sentences = translate_sentences(request)
        write_translation(word, language_to, translated_words, translated_sentences)


def translate_one_language(language_from, language_to, word):
    url = get_URL(language_from, language_to, word)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"}
    r = requests.get(url, headers=headers)
    if check_HTTP_status(r):
        print("200 OK")
        translated_words = translate_words(r)
        translated_sentences = translate_sentences(r)
        print_translated_words(language_to, translated_words)
        print_translated_sentences(language_to, translated_sentences)


def write_translation(word, language_to, translated_words, translated_sentences):
    all_translated_words = print_translated_words(language_to, translated_words)
    all_translated_sentences = print_translated_sentences(language_to, translated_sentences)
    print(all_translated_words)
    print(all_translated_sentences)
    with open(f"{word}.txt", "a", encoding="utf-8") as f:
        print(all_translated_words, file=f)
        print(all_translated_sentences, file=f)


def verify_input():
    args = sys.argv
    language_from = args[1].lower()
    language_to = args[2].lower()
    word = args[3].lower()
    if language_from in unavailable_languages:
        print(f"Sorry, the program doesn't support {language_from}")
        sys.exit()
    elif language_to in unavailable_languages:
        print(f"Sorry, the program doesn't support {language_to}")
        sys.exit()
    elif language_from not in available_languages:
        print(f"Sorry, unable to find {language_from}")
        sys.exit()
    elif language_to not in available_languages:
        print(f"Sorry, unable to find {language_to}")
        sys.exit()
    return language_from, language_to, word


def main():
    language_from, language_to, word = verify_input()
    if language_to != "all":
        translate_one_language(language_from, language_to, word)
    else:
        translate_all_languages(language_from, word)


if __name__ == "__main__":
    main()
