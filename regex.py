import re

inp = input("Enter file name:")
if len(inp) < 1:
    name = 'regex_sum_169737.txt'
file = open(name)

lst = []
count = 0
for line in file:
    y = re.findall('([0-9]+)', line)
    if len(y) > 0:
        count += 1
        for i in y:
            num = int(i)
            lst.append(num)
print(sum(lst) / count)
print(sum(lst))
print(count)
