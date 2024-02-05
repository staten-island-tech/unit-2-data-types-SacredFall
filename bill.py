#Let's create a function to accept a "bill" value and offer a tip of 0%, 15%, 20% or 25% depending on if the service was "bad, okay, good , or great ". 
 

""" print('What is your subtotal?')
subtotal = float(input())
print ('What is your tip percent?')
percent = float(input())

def tipcalc():
    global x
    x = (percent*subtotal/100)
    print(subtotal + int(x)) """
name = input('What is your name?')

def tiporgay():
    subtotal = float(input(f'How much was your subtotal {name}?'))
    print('How was our service?')
    print('Please respond with bad, okay, good, or great')
    ourservice = input(": ")
    if(ourservice == "bad"):
        print("We're sorry, you do not need to tip, please tell us what we could have done better in Skibidi Restaurant")
    elif(ourservice == okay):
        print('We reccommend a tip of ' + ourservice*0.15)
    elif(ourservice == good):
        print('We reccommend a tip of ' + ourservice*0.20)
    elif(ourservice == great):
        print('We reccommend a tip of ' + ourservice*0.25)

tiporgay()


        
    