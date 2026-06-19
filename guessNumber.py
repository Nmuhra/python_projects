import random

num = random.randint(1,100)

while True:
    try:
        choice = int(input('Choose a number between 1 and 100\n'))
        if(choice == num):
            print('Congrats, that is the correct number\n')
            break
        elif(choice > num):
            print('Too High!\n')
        else:
            print("Too low!\n")
    except:
        print("Input is incorrect!\n")
        