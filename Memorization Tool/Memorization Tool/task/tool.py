import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///flashcard.db?check_same_thread=False')
Base = declarative_base()


class Flashcard(Base):
    __tablename__ = 'flashcard'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


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
    flashcard = Flashcard(question=question, answer=answer)
    session.add(flashcard)
    session.commit()


def practice_flashcards():
    flashcards = session.query(Flashcard).all()
    if len(flashcards) == 0:
        print("There is no flashcard to practice!\n")
    for flashcard in flashcards:
        print(f'Question: {flashcard.question}')
        choice = input('press "y" to see the answer:\npress "n" to skip:\npress "u" to update:')
        try:
            if choice == "y":
                print(f'Answer: {flashcard.answer}\n')
            elif choice == "n":
                break
            elif choice == "u":
                update_menu(flashcard)
        except ValueError:
            print("Invalid choice\n")
    main()


def update_menu(flashcard):
    choice = input('press "d" to delete the flashcard:\npress "e" to edit the flashcard:')
    try:
        if choice == "d":
            delete_flashcard(flashcard)
        elif choice == "e":
            edit_flashcard(flashcard)
    except ValueError:
        print("Invalid choice\n")


def delete_flashcard(flashcard):
    session.delete(flashcard)
    session.commit()


def edit_flashcard(flashcard):
    print(f'current question: {flashcard.question}')
    flashcard.question = input("please write a new question:\n")
    print(f'current answer: {flashcard.answer}')
    flashcard.answer = input("please write a new answer:\n")
    session.commit()


if __name__ == "__main__":
    session = Session()
    main()
