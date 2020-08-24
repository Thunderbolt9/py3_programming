### Could aliasing cause potential confusion in this problem?
```
b = ['q', 'u', 'i']
z = b
b[1] = 'i'
z.remove('i')
print(z)
```
#### Answer : Yes

### Could aliasing cause potential confusion in this problem?
```
sent = "Holidays can be a fun time when you have good company!"
phrase = sent
phrase = phrase + " Holidays can also be fun on your own!"
```
#### Answer : No

### Which of these is a correct reference diagram following the execution of the following code?
```
lst = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
lst.remove('pluto')
first_three = lst[:3]
```
#### 1.
![](https://fopp.umsi.education/books/published/fopp/_images//week3a1_1.png)
#### 2.
![](https://fopp.umsi.education/books/published/fopp/_images//week3a1_2.png)
#### Answer : 1

### Which of these is a correct reference diagram following the execution of the following code?
```
x = ["dogs", "cats", "birds", "reptiles"]
y = x
x += ['fish', 'horses']
y = y + ['sheep']
```
#### 1.
![](https://fopp.umsi.education/books/published/fopp/_images//week3a3_1.png)
#### 2.
![](https://fopp.umsi.education/books/published/fopp/_images//week3a3_2.png)
#### 3.
![](https://fopp.umsi.education/books/published/fopp/_images//week3a3_3.png)
#### 4.
![](https://fopp.umsi.education/books/published/fopp/_images//week3a3_4.png)
#### Answer : 4

### Which of these is a correct reference diagram following the execution of the following code?
```
sent = "The mall has excellent sales right now."
wrds = sent.split()
wrds[1] = 'store'
new_sent = " ".join(wrds)
```
#### 1.
![](https://fopp.umsi.education/books/published/fopp/_images//week3a2_1.png)
#### 2.
![](https://fopp.umsi.education/books/published/fopp/_images//week3a2_2.png)
#### 3.
![](https://fopp.umsi.education/books/published/fopp/_images//week3a2_3.png)
#### 4.
![](https://fopp.umsi.education/books/published/fopp/_images//week3a2_4.png)

#### Answer : 1
