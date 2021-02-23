import sys

flashcards = []


def main():
    while True:
        choice = input("1. Add flashcards\n2. Practice flashcards\n3. Exit\n")
        try:
            if int(choice) == 1:
                add_flashcards()
            elif int(choice) == 2:
                practice_flashcards()
            elif int(choice) == 3:
                print("Bye!")
                sys.exit()
            else:
                print(f"{choice} is not an option")
        except ValueError:
            print(f"{choice} is not an option\n")


def add_flashcards():
    while True:
        choice = input("1. Add a new flashcard\n2. Exit\n")
        try:
            if int(choice) == 1:
                new_flashcard()
            elif int(choice) == 2:
                main()
            else:
                print(f"{choice} is not an option")
        except ValueError:
            print(f"{choice} is not an option")


def new_flashcard():
    while True:
        question = input("Question:\n")
        if len(question) > 0:
            break
        else:
            print("the question can't be empty!")
    while True:
        answer = input("Answer:\n")
        if len(answer) > 0:
            break
        else:
            print("the answer can't be empty!")
    flashcards.append({question: answer})


def practice_flashcards():
    if len(flashcards) == 0:
        print("There is no flashcard to practice!\n")
    for flashcard in flashcards:
        for question, answer in flashcard.items():
            print(f'Question: {question}')
            choice = input('Please press "y" to see the answer or press "n" to skip:\n')
            try:
                if choice == "y":
                    print(f'Answer: {answer}\n')
                elif choice == "n":
                    break
            except ValueError:
                print("Invalid choice\n")
    main()


if __name__ == "__main__":
    main()
