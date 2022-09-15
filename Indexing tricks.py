#Indexing tricks
fruit = "orange"
yelling = 'AHHHHHH!'
#this prints the first letter in the word, fruit[0] does the same thing.
print( fruit[-6])
#this prints from the letter range letter 0-3, giving us 'ora'
print(fruit[0:3])
#this prints the entire word
print(fruit[0:6])
#skips every other letter
print(fruit[0:6:2])
print(fruit[0:99])
#print in reverse
print(fruit[-1:-7:-1])
print(fruit[-1:3])
print(fruit[2:2])
#Slicing tricks
#ex_string[start: ] start to dend of string
#my_string[ : :-1] reverses
#to change strings, you have to SLICE THEM, this is not permaent
animal = 'cat'
print(animal)
animal = 'b' + animal [1:3]
print(animal)
#You can force Case on strings as well
print(fruit.upper())
print(yelling.lower())
#Since PYTHON is case sensitive, you can use this to avoid case sensitive errors by forcing the entire worder to be case upper or lower.
#now we use for-in loops, which are used  for iterating over iterables
for letter in fruit:
    print(letter)
index = -1
#While loops are great at repeating based on a condition
while index>= -len(fruit):
    print(fruit[index])
    index = index - 1
for letter in fruit[::-1]:
    print(fruit)
#Counts every letter and prints them
#Now print every e in 'Every Heaven'
Be = 'Every Heaven'
for letter in Be:
    if letter == 'E' or letter =='e':
        print(letter)

