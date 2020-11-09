import itertools

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Todo(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def menu():
    while True:
        user_input = int(input("1) Today's tasks\n"
                               "2) Week's tasks\n"
                               "3) All tasks\n"
                               "4) Missed tasks\n"
                               "5) Add task\n"
                               "6) Delete task\n"
                               "0) Exit\n"))
        if user_input == 0:
            print("Bye!")
            break
        if user_input == 1:
            todays_tasks()
        if user_input == 2:
            weeks_tasks()
        if user_input == 3:
            print("All tasks:")
            all_tasks()
        if user_input == 4:
            missed_tasks()
        if user_input == 5:
            add_task()
        if user_input == 6:
            print("Choose the number of the task you want to delete:")
            all_tasks()
            delete_task(int(input()))


def todays_tasks():
    today = datetime.today()
    rows = session.query(Todo).filter(Todo.deadline == today.date()).order_by(Todo.deadline).all()
    print(f"Today {datetime.strftime(today, '%d %b')}:")
    counter = (x for x in itertools.count(start=1))
    if rows:
        for row in rows:
            print(f'{next(counter)}. {row.task}')
        print()
    else:
        print("Nothing to do!")

def weeks_tasks():
    today = datetime.today()
    for i in range(0, 7):
        current_date = today + timedelta(days=i)
        print(f"{datetime.strftime(current_date, '%A %#d %b')}:")
        rows = session.query(Todo).filter(Todo.deadline == current_date.date()).all()
        counter = (x for x in itertools.count(start=1))
        if rows:
            for row in rows:
                print(f'{next(counter)}. {row.task}')
            print()
        else:
            print("Nothing to do!\n")

def all_tasks():
    rows = session.query(Todo).order_by(Todo.deadline).all()
    number = 1
    if rows:
        for row in rows:
            deadline = datetime.strftime(row.deadline, '%#d %b')
            print(f'{number}. {row.task}. {deadline}')
            number += 1
        print()
    else:
        print("Nothing to do!")
        print()

def add_task():
    task = input("Enter task\n")
    deadline = datetime.strptime(input("Enter deadline\n"), '%Y-%m-%d')
    new_task = Todo(task=task, deadline=deadline)
    session.add(new_task)
    session.commit()
    print("The task has been added!")


def missed_tasks():
    rows = session.query(Todo).filter(Todo.deadline < datetime.today().date()).all()
    counter = (x for x in itertools.count(start=1))
    if rows:
        for row in rows:
            deadline = datetime.strftime(row.deadline, '%#d %b')
            print(f'{next(counter)}. {row.task}. {deadline}')
        print()
    else:
        print("Nothing is missed!")
        print()

def delete_task(choice):
    rows = session.query(Todo).order_by(Todo.deadline).all()
    session.delete(rows[choice - 1])
    session.commit()

    print("The task has been deleted!")



menu()
