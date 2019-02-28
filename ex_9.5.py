'''This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.'''

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
                word = word.split('@')
                for i in word:
                    if i == word[1]:
                        count[i] = count.get(i, 0) + 1

print(count)
