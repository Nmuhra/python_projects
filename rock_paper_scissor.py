import random

def rules(x,y):
    if x == y:
        print('Draw\n')
    elif (x == 'r' and y == 's') or (x == 'p' and y == 'r') or (x == 's' and y == 'p'):
        print('You Win!\n')
    else:
        print('You lose!\n')

map = {
    'r': '🪨',
    'p': '📃',
    's': '✂️'
}

## Declared as a tuple so that it is read only 
options = ('r','p','s')

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