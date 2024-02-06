#Create a function that accepts 2 arguments. Find the greatest common factor between those numbers. 

def isInt(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

input('GCF CALCULATOR FOR TWO TERMS [PRESS ENTER TO CONTINUE]')
x = int(input('What is your first number?'))
y = int(input('What is your second number?'))

def myfunnyfunction(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller + 1):
        if ((x%i == 0) and (y%i == 0)):
            hcf = i
    return hcf

print(f'Your GCF is {myfunnyfunction(x,y)}')

