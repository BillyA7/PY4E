'''9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer..

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt'''

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

bigword = None
bigcount = -1
for a, b in count.items():
    if b > bigcount:
        bigword = a
        bigcount = b


print(bigword, bigcount)
