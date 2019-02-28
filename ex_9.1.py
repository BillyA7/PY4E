'''Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt

Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn't matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.'''

inp = input('Enter a filename: ')
if len(inp) < 1:
    name = 'words.txt'
fname = open(name)

words = {}
for line in fname:
    new = line.split()
    for word in new:
        words[word] = 0

print(words)
