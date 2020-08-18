'''Q-1: There is a function we are providing in for you in this problem called square. It takes one integer and returns the square of that integer value. Write code to assign a variable called xyz the value 5*5 (five squared).
Use the square function, rather than just multiplying with '''

xyz = square(5)
print(xyz)

'''Q-2: Write code to assign the number of characters in the string rv to a variable num_chars'''

rv = """Once upon a midnight dreary, while I pondered, weak and weary,
    Over many a quaint and curious volume of forgotten lore,
    While I nodded, nearly napping, suddenly there came a tapping,
    As of some one gently rapping, rapping at my chamber door.
    'Tis some visitor, I muttered, tapping at my chamber door;
    Only this and nothing more."""

# Write your code here!
num_chars=len(rv)
print(num_chars)


'''Q-3: data-19-1: The code below initializes two variables, z and y. We want to assign the total number of characters in z and in y to the variable a.
Which of the following solutions, if any, would be considered hard coding?'''

z = "hello world"
y = "welcome!"

#a = len("hello worldwelcome!")
#a = 11 + 8
#a = len("hello world") + len("welcome!")
