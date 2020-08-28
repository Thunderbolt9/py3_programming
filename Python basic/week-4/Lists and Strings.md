####  Q-1. Which method would you use to figure out the position of an item in a list?
```
A. .pop()
B. .insert()
C. .count()
D. .index()
```
#### Answer: D

#### Q-2.  Which method is best to use when adding an item to the end of a list?
```
A. .insert()
B. .pop()
C. .append()
D. .remove()
```
#### Answer: C

#### Q-3. Write code to add ‘horseback riding’ to the third position (i.e., right before volleyball) in the list sports
```
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
a = sports.insert(2, 'horseback riding')
print(a)
```

#### Q-4. Write code to take ‘London’ out of the list trav_dest.
```
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']
a = trav_dest.remove('London')
print(a)
```

#### Q-5. Write code to add ‘Guadalajara’ to the end of the list trav_dest using a list method.
```
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']
a = trav_dest.append('Guadalajara')
print(a)
```

#### Q-6. Write code to rearrange the strings in the list winners so that they are in alphabetical order from A to Z.
```
winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']
a = winners.sort()
print(a)
```

#### Q-7. Write code to switch the order of the winners list so that it is now Z to A. Assign this list to the variable z_winners.
```
winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']

z_winners = winners[::-1]
print(z_winners)
```
