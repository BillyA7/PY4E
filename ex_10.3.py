'''10.3 Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.'''

import string

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

count = 0
dict = {}
alphabet = string.ascii_lowercase
for line in handle:  # for each line in the file
    line = line.lower()  # convert to lower case
    line = line.split()  # seperate each word by whitespace
    for word in line:  # for each word in the line
        for letter in word:  # for each letter in the word
            if letter in alphabet:  # if the letter is in the alphabet variable
                count += 1  # add one to count
                # add to dict or increase current value by one
                dict[letter] = dict.get(letter, 0) + 1

# switch position of keys and values and store in new list
tmp = []
for k, v in dict.items():
    tmp.append(((v / count) * 100, k))  # calculate frequency of value in %

# sort list values from high to low
lst = sorted(tmp, reverse=True)

# switch position back of keys and values and print
for k, v in lst:
    print(v, round(k, 2))  # round value to two decimal places
