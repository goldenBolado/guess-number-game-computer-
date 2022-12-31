import random

def guess(x):
    random_number = random.randint(1, x)
    tries = 0
    while True:
        guess = int(input(f'Choose a number between 1 and {x}: '))
        if guess > random_number:
            print('Try a smaller guess')
            tries += 1
        elif guess < random_number:
            print('Try a bigger guess')
            tries += 1
        elif guess == random_number:
            break
    print(f'CORRECT!!! It took you {tries} tries')

guess(10)