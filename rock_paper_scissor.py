import random


ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

map = {
     ROCK : '🪨',
    PAPER: '📃',
    SCISSORS: '✂️'
}

def rules(x,y):
    if x == y:
        print('Draw\n')
    elif (x == ROCK and y == SCISSORS) or (x == PAPER and y == ROCK) or (x == SCISSORS and y == PAPER):
        print('You Win!\n')
    else:
        print('You lose!\n')

options = tuple(map.keys())

while True:
    cpuChoice = random.choice(options)

    print('Rock, paper, or scissors? (r/p/s): ')
    userChoice = input()

    if userChoice not in options:
        print('Invalid Choice!')
    else:
        userEmoji = map[userChoice]
        cpuEmoji = map[cpuChoice]
        print(f'You chose {userEmoji}')
        print(f'Computer chose {cpuEmoji}')
        rules(userChoice,cpuChoice)