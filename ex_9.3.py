'''9.3 Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.'''

name = input("Enter file name: ")
if len(name) < 1:
    name = "C:\\Users\\bills\\Desktop\\PY4E\\mbox-short.txt"
handle = open(name)

count = {}
for line in handle:
    if line.startswith('From '):
        new = line.split()
        for word in new:
            if '@' in word:
                count[word] = count.get(word, 0) + 1

print(count)
