'''10.3 Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.'''

# v2 using regex

import re

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

dict = {}
count = 0
for line in handle:
    line = line.lower()
    line = line.rstrip()
    for word in line:
        for letter in word:
            y = re.findall('([a-z]+)', letter)  # find every character a-z
            if len(y) > 0:  # get rid of empty lists
                count += 1
                new = y[0]
                dict[new] = dict.get(new, 0) + 1

# switch position of keys and values and store in new list
tmp = []
for k, v in dict.items():
    tmp.append(((v / count) * 100, k))

# sort list values from high to low
lst = sorted(tmp, reverse=True)

# switch position back of keys and values and print
for k, v in lst:
    print(v, round(k, 2))
