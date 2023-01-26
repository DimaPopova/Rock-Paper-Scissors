import random

rock = 'Rock'
paper = 'Paper'
sciossors = 'Sciossors'

player_move = input('Choose [r]ock, [p]aper or [s]ciossors: ')

if player_move == 'r':
    player_move = rock
elif player_move == 'p':
    player_move = paper
elif player_move == 's':
    player_move = sciossors
else:
    raise SystemExit('Invalid Input. Try again..')

computers_move = random.randint(1, 3)

computer_random_move = ''

if computers_move == 1:
    computer_random_move = rock
elif computers_move == 2:
    computer_random_move = paper
else:
    computer_random_move = sciossors

print(f'The computer chose {computer_random_move}.')

if (player_move == rock and computer_random_move == sciossors) or \
        (player_move == paper and computer_random_move == rock) or \
        (player_move == sciossors and computer_random_move == paper):
    print('You win!')

elif player_move == computer_random_move:
    print('Draw!')
else:
    print('You lose!')
