from random import randint

print('Choose either Door 1, Door 2, or Door 3 to see if you are a winner.')

a = int(input('Enter your door choice here: '))

if 1 <= a <= 3:
    print('Great Choice')
else:
    print('Choose a number from 1 to 3')

iterations = 10000
count = 0
for i in range(iterations):
    prize = randint(1, 3)
    if prize == 1:
        s = randint(2, 3)
        doors = prize, s
        if a == s:
            a = prize
        else:
            a = s
    elif prize == 2:
        possible_doors = [1, 3]
        q = choice(possible_doors)
        doors = q, prize
        if a == q:
            a = prize
        else:
            a = q
    else:
        v = randint(1, 2)
        doors = v, prize
        if a == v:
            a = prize
        else:
            a = v
    if a == prize:
        count = count + 1

percent = (count / iterations)*100

print(f'Congrats! You won percent {percent}% of the time.')




