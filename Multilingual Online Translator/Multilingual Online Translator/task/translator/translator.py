print('Hello, World!')

def choose_language():
    language = input('Type "en" if you want to translate from French into English,'
                     'or "fr" if you want to translate from English into French:')
    return language


def chose_words_to_translate():
    words = input('Type the word you want to translate:')
    return words

def main():
    language = choose_language()
    words = chose_words_to_translate()
    print(f'You chose "{language}" as the language to translate "{words}" to.')


main()
