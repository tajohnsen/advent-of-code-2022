from itertools import *
from string import ascii_letters

with open("input", "r") as in_file:
    data = in_file.readlines()

stripped = map(lambda i: i.strip(), data)
total = 0
for line in stripped:
    length = len(line)
    midway = int(length / 2)
    x, y = line[:midway], line[midway:]
    for letter in x:
        if letter in y:
            total += ascii_letters.find(letter) + 1
            break

total2 = 0
stripped = map(lambda i: i.strip(), data)
while True:
    try:
        x, y, z = list(islice(stripped, 0, 3))
    except ValueError:
        break
    for a in x:
        if a in y:
            if a in z:
                total2 += ascii_letters.find(a) + 1
                break

print(total)
print(total2)
