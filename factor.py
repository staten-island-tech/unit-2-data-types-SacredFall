#Create a function that accepts an input and determines all factors of the number. 
num = int(input('Enter the number you want inputted: '))
def factorlization():
    print(f'The factors of {num} are: ')
    for i in range(1, num + 1):
        if num % i  == 0:
            print(i)

factorlization()

    


