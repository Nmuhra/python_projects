import random


print('Roll the Dice? y/n?')
choice  = input()

while(choice == 'y'):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print(f'({dice1},{dice2})')
    print('Roll the Dice? y/n?')
    choice = input()

if(choice != 'y' and choice != 'n'):
    print("Invalid input!")
else:
    print("Thanks for playing!")



