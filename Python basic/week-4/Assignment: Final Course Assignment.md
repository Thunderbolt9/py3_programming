### Below are a set of scores that students have received in the past semester. Write code to determine how many are 90 or above and assign that result to the value a_scores.

```python
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"

# Convert the string of scores to a list of integers
scores_list = list(map(int, scores.split()))

# Count the number of scores that are 90 or above
a_scores = sum(score >= 90 for score in scores_list)

print("Number of scores 90 or above:", a_scores)
```
### Write code that uses the string stored in org and creates an acronym which is assigned to the variable acro. Only the first letter of each word should be used, each letter in the acronym should be a capital letter, and there should be nothing to separate the letters of the acronym. Words that should not be included in the acronym are stored in the list stopwords. For example, if org was assigned the string “hello to world” then the resulting acronym should be “HW”.
```python
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"

# Split the string into words and filter out stopwords
words = [word for word in org.split() if word.lower() not in stopwords]

# Create the acronym by taking the first letter of each word and making it uppercase
acro = ''.join(word[0].upper() for word in words)

print("Acronym:", acro)
```
### Write code that uses the string stored in sent and creates an acronym which is assigned to the variable acro. The first two letters of each word should be used, each letter in the acronym should be a capital letter, and each element of the acronym should be separated by a “. ” (dot and space). Words that should not be included in the acronym are stored in the list stopwords. For example, if sent was assigned the string “height and ewok wonder” then the resulting acronym should be “HE. EW. WO”.

```python
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

# Split the string into words and filter out stopwords
words = [word for word in sent.split() if word.lower() not in stopwords]

# Create the acronym by taking the first two letters of each word, making them uppercase,
# and joining them with ". "
acro = '. '.join(word[:2].upper() for word in words)

print("Acronym:", acro)
```
### A palindrome is a phrase that, if reversed, would read the exact same. Write code that checks if p_phrase is a palindrome by reversing it and then checking if the reversed version is equal to the original. Assign the reversed version of p_phrase to the variable r_phrase so that we can check your work.

```python
p_phrase = "was it a car or a cat I saw"

# Remove spaces and convert to lowercase for accurate palindrome check
cleaned_p_phrase = ''.join(p_phrase.split()).lower()

# Reverse the cleaned phrase
r_phrase = cleaned_p_phrase[::-1]

# Check if the original and reversed versions are equal
is_palindrome = cleaned_p_phrase == r_phrase

print("Original phrase:", p_phrase)
print("Reversed phrase:", r_phrase)
print("Is palindrome:", is_palindrome)
```
### Provided is a list of data about a store’s inventory where each item in the list represents the name of an item, how much is in stock, and how much it costs. Print out each item in the list with the same formatting, using the .format method (not string concatenation). For example, the first print statment should read The store has 12 shoes, each for 29.99 USD.
```python
inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

for item in inventory:
    # Split the item details into name, stock, and price
    name, stock, price = item.split(', ')
    
    # Format and print each item
    print("The store has {}, each for {} USD.".format(f"{stock} {name}", price))

```

