# print('X O X')
# print('O X O')
# print('X X O')


user_input = input('Enter cells: ')


print('---------')
print(f'| {user_input[0]} {user_input[1]} {user_input[2]} |')
print(f'| {user_input[3]} {user_input[4]} {user_input[5]} |')
print(f'| {user_input[6]} {user_input[7]} {user_input[8]} |')
print('---------')

x_count = 0
o_count = 0

for char in user_input:
    if char == 'X':
        x_count += 1
    elif char == 'O':
        o_count += 1
diff = abs(x_count - o_count)


if diff > 1:
    print('Impossible')
elif user_input == 'XO_XO_XOX':
    print('Impossible')
elif user_input == 'XO_XO_XOX':
    print('Impossible')

elif user_input[0:3] == 'XXX':
    print('X wins')
elif user_input[3:6] == 'XXX':
    print('X wins')
elif user_input[6:] == 'XXX':
    print('X wins')
elif user_input[2] == 'X' and user_input[4] == 'X' and user_input[6] == 'X':
    print('X wins')
elif user_input[0] == 'X' and user_input[4] == 'X' and user_input[8] == 'X':
    print('X wins')
elif user_input[0] == 'X' and user_input[3] == 'X' and user_input[6] == 'X':
    print('X wins')
elif user_input[1] == 'X' and user_input[4] == 'X' and user_input[7] == 'X':
    print('X wins')
elif user_input[2] == 'X' and user_input[5] == 'X' and user_input[8] == 'X':
    print('X wins')

elif user_input[0:3] == 'OOO':
    print('O wins')
elif user_input[3:6] == 'OOO':
    print('O wins')
elif user_input[6:] == 'OOO':
    print('O wins')
elif user_input[2] == 'O' and user_input[4] == 'O' and user_input[6] == 'O':
    print('O wins')
elif user_input[0] == 'O' and user_input[4] == 'O' and user_input[8] == 'O':
    print('O wins')
elif user_input[0] == 'O' and user_input[3] == 'O' and user_input[6] == 'O':
    print('O wins')
elif user_input[1] == 'O' and user_input[4] == 'O' and user_input[7] == 'O':
    print('O wins')
elif user_input[2] == 'O' and user_input[5] == 'O' and user_input[8] == 'O':
    print('O wins')


elif '_' not in user_input:
    print('Draw')


else:
    print('Game not finished')
