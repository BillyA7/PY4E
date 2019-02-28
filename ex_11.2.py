'''11.2 Write a program to look for lines of the form:

New Revision: 39772

Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average.'''

import re

inp = input("Enter file name:")
if len(inp) < 1:
    name = 'mbox-short.txt'
file = open(name)

lst = []
count = 0
for line in file:
    y = re.findall('^New .*: ([0-9]+)', line)
    if len(y) > 0:
        count += 1
        for i in y:
            num = int(i)
            lst.append(num)
print(sum(lst) / count)
print(sum(lst))
print(count)
