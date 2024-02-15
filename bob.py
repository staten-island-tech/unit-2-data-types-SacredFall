hunger = int(input('Amount of hunger bars'))
apple = int(input('How much apples will bob eat'))
seconds = int(input('How much will bob wait'))

if apple > hunger:
    apple = hunger


final = int(apple - seconds)

if final < 0:
    final = 0

print(final)

