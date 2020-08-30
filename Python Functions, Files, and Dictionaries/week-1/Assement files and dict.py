''' Q-1. The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary.
Find the total number of characters in the file and save to the variable num.'''

with open("travel_plans.txt","r") as file:
    file_char=file.read()
    num = len(file_char)
    print(num)
    file.close()
    
''' Q-2. We have provided a file called emotion_words.txt that contains lines of words that describe emotions. 
Find the total number of words in the file and assign this value to the variable num_words.'''

num_words=0
with open("emotion_words.txt","r") as file:
    for words in file:
        num_words+=len(words.split())
    file.close()

''' Q-3. Assign to the variable num_lines the number of lines in the file school_prompt.txt.'''

file=open("school_prompt.txt","r")
char_y=file.readlines()
num_lines=len(char_y)
print(num_lines)
file.close()

''' Q-4. Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars'''

file=open("school_prompt.txt","r")
char_y=file.read()
beginning_chars=str(char_y[:30])
print(beginning_chars)
file.close()

''' Q-5. Write code that will count the number of vowels in the sentence s and assign the result to the variable num_vowels. For this problem,
vowels are only a, e, i, o, and u. Hint: use the in operator with vowels.'''

s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']
s = list(s)
num_vowels = 0
for i in s:
    for j in i:
        if j in vowels:
            num_vowels+=1

print(num_vowels)    
