''' Q-1. Write a function called int_return that takes an integer as input and returns the same integer.'''

def int_return(i):
    return i
z=int(input())
int_return(z)


''' Q-2. Write a function called add that takes any number as its input and returns that sum with 2 added.'''

def add(x):
    sum = x+2
    return sum
a=int(input())
add(a)


''' Q-3. Write a function called change that takes any string, adds “Nice to meet you!” to the end of the argument given, and returns that new string.'''

def change(v):
    return v+'Nice to meet you!'

v=input("Enter the string: ")
change(v)


''' Q-4. Write a function, accum, that takes a list of integers as input and returns the sum of those integers.'''

def accum(lst):
    j=0
    for i in lst:
        j=j+i
    return j
lst=[1,2,3,4,5,6,7,8,9]
accum(lst)


''' Q-5. Write a function, length, that takes in a list as the input.
If the length of the list is greater than or equal to 5, return “Longer than 5”.
If the length is less than 5, return “Less than 5”.'''


def length(lst):
    if len(lst)>=5:
        return 'Longer than 5'
    else:
        return 'Less than 5'

lst=list(input())
length(lst)

   
'''Q-6 You will need to write two functions for this problem. The first function, divide that takes in any number and returns that same number divided by 2.
The second function called sum should take any number, divide it by 2, and add 6. It should return this new number. You should call the divide function within the sum function.
Do not worry about decimals.'''

def divide(n):
    return n/2
def sum(n):
    return n/2+6

sum(divide(10))
