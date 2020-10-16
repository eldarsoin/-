import random
name = input('Как тебя зовут?\n'   )
print ('Добро пожаловать', name , 'попробуй угадать загаданное число')

number = random.randint(1, 100)
guess = int(input('твой вариант: '))
tries = 1

while guess != number:
    if guess > number:
        print('Меньше')
    else:
        print('Больше')
    guess = int(input('твой вариант: '))
    tries += 1
print (name, 'Ты угадал с', tries ,'попытки')
print ('загаданное число',   number  )
print( \
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       | .     . |
       |  `...`  |
       -----------
                   """)
