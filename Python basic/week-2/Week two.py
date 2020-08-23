''' Q-1: Write one for loop to print out each character of the string my_str on a separate line.'''

my_str = "MICHIGAN"
lst = list(my_str)
count = 0
for i in lst:
    print(i)
    count = count +1

''' Q-2: Write one for loop to print out each element of the list several_things. Then, write another
for loop to print out the TYPE of each element of the list several_things. To complete this problem you
should have written two different for loops, each of which iterates over the list several_things, but
each of those 2 for loops should have a different result.'''

several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]
lst = list(several_things)
count = 0
for i in lst:
    print(i)
    count = count + 1

for j in lst:
    print(type(j))
    count = count + 1

''' Q-3: Write code that uses iteration to print out the length of each element of the list stored in str_list.'''

str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

count = 0
for i in str_list:
    print(len(i))
    count = count + 1

''' Q-4: Write code to count the number of characters in original_str using the accumulation pattern and assign the
answer to a variable num_chars. Do NOT use the len function to solve the problem (if you use it while you are working
on this problem, comment it out afterward!) '''

original_str = "The quick brown rhino jumped over the extremely lazy fox."
count = 0
for _ in original_str:
    count = count + 1
   
num_chars = count
print(num_chars)

''' Q-5: addition_str is a string with a list of numbers separated by the + sign. Write code that uses the accumulation
pattern to take the sum of all of the numbers and assigns it to sum_val (an integer). (You should use the .split("+")
function to split by "+" and int() to cast to an integer).'''

addition_str = "2+5+10+20"
add_str = addition_str.split("+")
add_str = [int(n) for n in add_str]
accum = 0
for i in add_str:
    accum = accum + i
    
sum_val = accum
print(sum_val)

''' Q-6: week_temps_f is a string with a list of fahrenheit temperatures separated by the , sign. Write code that uses
the accumulation pattern to compute the average (sum divided by number of items) and assigns it to avg_temp. Do not hard
code your answer (i.e., make your code compute both the sum or the number of items in week_temps_f) (You should use the
.split(",") function to split by "," and float() to cast to a float).'''

week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
temp_f = week_temps_f.split(",")
temp_f = [float(n) for n in temp_f]
avg = 0
sum = 0
for num in temp_f:
    sum=sum+num
avg_temp = sum/len(temp_f)
print(avg_temp)

''' Q-7: Write code to create a list of numbers from 0 to 67 and assign that list to the variable nums. Do not hard code the list.'''

nums = list(range(68))
print(nums)

''' Q-8: Write code to create a list of word lengths for the words in original_str using the accumulation pattern and assign the
answer to a variable num_words_list. (You should use the len function).'''

original_str = "The quick brown rhino jumped over the extremely lazy fox"
b = original_str.split(" ")
num_words_list=[]
for i in b:
    a = len(i)
    num_words_list.append(a)

print(num_words_list)

''' Q-9: Create an empty string and assign it to the variable lett. Then using range, write code such that when your code is run,
lett has 7 b’s ("bbbbbbb").'''

lett =""
for _ in range(7):
    lett+='b'
print(lett)

'''Q-10: Write a program that uses the turtle module and a for loop to draw something. It doesn’t have to be complicated, but draw
something different than we have done in the past. (Hint: if you are drawing something complicated, it could get tedious to watch
it draw over and over. Try setting .speed(10) for the turtle to draw fast, or .speed(0) for it to draw super fast with no animation.)'''

import turtle
import math
alex = turtle.Turtle()
turtle.Screen()

for i in [0,1,2,3]:
    alex.forward(100)
    alex.right(90)
alex.left(90)
dist =  math.sqrt((100*100)//2)
alex.right(45)
alex.forward(dist)
alex.right(90)
alex.forward(dist)
alex.left(45)
alex.forward(100)
alex.left(90)
alex.forward(33.5)
alex.right(90)
alex.forward(33.5)
alex.left(90)
alex.forward(33.5)
alex.left(90)
alex.forward(33.5)
