from random import randint

print('Choose either Door 1, Door 2, or Door 3 to see if you are a winner.')

a = int(input('Enter your door choice here: '))

if 1 <= a <= 3:
    print('Great Choice')
else:
    print('Choose a number from 1 to 3')

count = 0
for i in range(10000):
    prize = randint(1, 3)
    if prize == 1:
        s = randint(2, 3)
        doors = prize, s
    elif prize == 2:
        q = randint(1, 3)
        doors = q, prize
    else:
        v = randint(1, 2)
        doors = v, prize
    if a == prize:
        count = count + 1

percent = (count / 10000)*100

print(f'Congrats! You won percent {percent}% of the time.')