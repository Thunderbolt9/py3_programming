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

''' Q-3. Write code to count the number of strings in list items that have the character w in it. Assign that number to the variable acc_num.
HINT 1: Use the accumulation pattern!
HINT 2: the in operator checks whether a substring is present in a string.
Hard-coded answers will receive no credit.'''

items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num = 0
for i in items:
    if 'w' in i:
        acc_num+=1

print(acc_num)

''' Q-4. Write code that counts the number of words in sentence that contain either an “a” or an “e”. Store the result in the variable num_a_or_e.
Note 1: be sure to not double-count words that contain both an a and an e.
HINT 1: Use the in operator.
HINT 2: You can either use or or elif.
Hard-coded answers will receive no credit.'''

sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
words = sentence.split(" ")
num_a_or_e = 0
for i in words:
    if (('a' in i) or ('e' in i)) :
        num_a_or_e+=1

print(num_a_or_e)

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
