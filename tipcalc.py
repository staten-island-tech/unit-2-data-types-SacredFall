print('What is your subtotal?')
subtotal = float(input())
print ('What is your tip percent?')
percent = float(input())

def tipcalc():
    global x
    x = (percent*subtotal/100)
    print(subtotal + int(x))

tipcalc()