#!/usr/bin/env python3
from itertools import *

with open('input', 'r') as in_file:
	data = in_file.readlines()
	
it = iter(data)

stripped = map(lambda x: x.strip(), it)

def summations(stripped):
	while True:
		ints = map(int, takewhile(lambda x: x != '', stripped))
		total = sum(ints)
		if total == 0:
			break
		yield total

print(sum(sorted(summations(stripped))[-3:]))
