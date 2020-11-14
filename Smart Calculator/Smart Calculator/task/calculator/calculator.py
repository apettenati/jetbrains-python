import sys

def get_user_input():
    user_input = input()
    if user_input == '/exit':
        print("bye")
        sys.exit()
    if user_input == '/help':
        print("The program calculates the sum of numbers")
    else:
        input_list = user_input.split()
        int_list = [int(x) for x in input_list]
        return int_list

def addition(iterable):
    return sum(iterable)

def main():
    while True:
        input_list = get_user_input()
        if input_list:
            print(addition(input_list))
        else:
            pass

if __name__ == "__main__":
    main()
