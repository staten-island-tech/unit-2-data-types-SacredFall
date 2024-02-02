
# Integers and Floats
You have already been exposed to integers (numbers) through the previous exercises. Integers represent whole numbers in Python. Floats represent numbers with decimal values. Pop the following into python and check the output and how they are different. Note: It's important to understand the basics of these datatypes now as they have properties exclusive to their data type. 
```python
x = 3
y = float(3)
print(x,y)
```
## Tip Calculator 
You will be creating a tip calculator that must accomplish all of the following

- Create variables representing at the bill, tip and total amount
paid
- Receive user input and assign that user input to the variables in
step 1 (excluding total)
- Change the data type of bill from String to Float
- Change the data type of tip to Integer (int)
- Calculate the total that needs to be paid
- Print the f string after the user has input data
# Lists
These ints and floats can be stored in lists to let you manage complexitymore easily. Try the following code and check the output. 
```python
values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)
```
You may noticed the following

1.  We can store different data types inside a list, they do not need to be the same.
2.  if we print the variable "values" we can see the entire list
3.  If we use a for loop we can easily iterate through the list and access the values.

## What if we just want one single, specific value?
We can access individual elements in the list by using brackets ([]) and the elements position. Note that in CS we tend to begin counting at 0. 
```python
print(values[0])
print(values[6])
```
By printing the values at position 0 and 6 we can access the first and last elements. Try accessing element 7 and see what happens. Would you have been able to debug this?

# Strings
Strings are a list of characters that represent text. It's important to  understand that a String is not simply "just text", it is instead a list of characters. For example, "test" is really a list with each letter stored as an element in a list.
```
"test"
["t","e","s","t"]
```
## Why does this matter?
Think to yourself, how does knowing that each character in a String is really an element in a list? What does that allow us to do? Why do computers want Strings represented this way?

## String Methods
[Python String Methods](https://docs.python.org/3.11/library/string.html) is a link that will take you the Python documentation site (Great Resource!). Here we can see there a number of functions built into Python for working with Strings. Some of which are made possible because of how the computer stores and interprets Strings. 

Let's put some of these into practice.
```python
x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z)
```
Here we can use the split function which allows for an parameter to be passed in. The parameter passed in will be used to split the string into a new list. By using an empty space we can break up our words into seperate elements. Since we know how to access elements in a list we can then store the first word as a seperate variable to be used later.

# Challenge
1. Using the "input" method in Python, ask a user to input a sentence. Then develop a function that accepts a the user input and will tell you how many words are in that string. First write out your plan in Pseudo-code using comments. Then craft the function. 
2. Mad Libs Project

# Booleans and Control Flow
InPython we can evaluate statements to True or False.These are referred to as boolean data types. Something can evaulate to either True OR false, never both. We can use conditional statements, if, elif (else if) and  else to create a control flow in our applications. 

```python
day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect")
```
Here, the user will either input Friday or not. It is either Friday or it is not. If the day of the week is Friday then we will print "correct". In all other situations we will print "incorrect"
## F Strings
Variables can be used inside Strings by adding an F before the String and using {} templates inside the String. See below
``` Python
x = "test"
print(f"hello {x}")
```
```python

temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold')
```
What will happen when we run the above code? 

## Challenge
Let's create a function that determines if a number is odd or even
## Challenge
Let's create a function to accept a "bill" value and offer a tip of 0%, 15%, 20% or 25% depending on if the service was "bad, okay, good , or great ". 

## Challenge

Create a function that accepts an input and determines all factors of the number. 

## Challenge 

Create a function that accepts 2 arguments. Find the greatest common factor between those numbers. 

