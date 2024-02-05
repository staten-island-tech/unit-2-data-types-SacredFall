#Let's create a function to accept a "bill" value and offer a tip of 0%, 15%, 20% or 25% depending on if the service was "bad, okay, good , or great ". 
 

""" print('What is your subtotal?')
subtotal = float(input())
print ('What is your tip percent?')
percent = float(input())

def tipcalc():
    global x
    x = (percent*subtotal/100)
    print(subtotal + int(x)) """
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def subtotal():
    subtotal = input("> $")
    if isfloat(subtotal):
        subtotal = float(subtotal)
    else:
        print('Restart please, remember do not be an idiot and put a number this time!')


print('What is your name?')
name = input("> ")
print(f'How much was your subtotal {name}? (In dollars please)')
subtotal()




def tiporgay():

    subtotal = input("> $")
    if isfloat(subtotal):
        subtotal = float(subtotal)
    else:
        print('Restart please, remember do not be an idiot and put a number this time!')
        tiporgay()

    print('How was our service?')
    print('Please respond with bad, okay, good, or great')
    ourservice = input("> ")
    if(ourservice == "bad"):
        print("We're sorry, you do not need to tip, please tell us what we could have done better in Skibidi Restaurant")
    elif(ourservice == "okay"):
        print(f'We reccommend a tip of ${subtotal*float(0.15)}')
    elif(ourservice == "good"):
        print(f'We reccommend a tip of ${subtotal*float(0.20)}')
    elif(ourservice == "great"):
        print(f'We reccommend a tip of ${subtotal*float(0.25)}')
    else:
        print('incorrect input, please try again')

tiporgay()


        
    