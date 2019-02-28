'''Revise a previous program as follows: Read and parse the "From" lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.

After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.'''

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

lst = []
for k, v in count.items():
    lst.append((v, k))

lst = sorted(lst, reverse=True)

print(lst[0])
