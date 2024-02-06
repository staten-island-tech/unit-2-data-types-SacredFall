#Let's create a function to accept a "bill" value and offer a tip of 0%, 15%, 20% or 25% depending on if the service was "bad, okay, good , or great ". 
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def subtotal1():
    global subtotal
    subtotal = input("> $")
    if isfloat(subtotal):
        subtotal = float(subtotal)
        tipplease()
    else:
        print('Restart please, remember do not be an idiot and put a number this time!')
        subtotal1()

def tipplease():

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
        tipplease()


print('What is your name?')
name = input("> ")
print(f'How much was your subtotal {name}? (In dollars please)')
subtotal1()








        
    