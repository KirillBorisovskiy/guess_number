from random import randint 

num = randint(1, 100)

while True:
    
    guess = int(input('Я загадал число от 1 до 100 угадай его '))
    
    if num > guess:
        print('Ваше число меньше загаданного')
    elif num < guess:
        print('Ваше число больше загаданного')
    else:
        print('Поздравляю вы угадали')
        break