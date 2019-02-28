'''9.2 Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with "From", then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).'''

name = input("Enter file name: ")
if len(name) < 1:
    name = "C:\\Users\\bills\\Desktop\\PY4E\\mbox-short.txt"
handle = open(name)

count = {}
for line in handle:
    if line.startswith('From '):
        new = line.split()
        for word in new:
            if len(word) == 3:
                count[word] = count.get(word, 0) + 1

print(count)
