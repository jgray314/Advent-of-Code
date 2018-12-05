import sys
from collections import defaultdict

CAP_DIFF = 32

def read():
	return sys.stdin.readline()

def react(s):
	react_idx = set([])
	skip_one = False
	for i in range(len(s) - 1):
		if skip_one:
			skip_one = False
			continue
		a = s[i]
		b = s[i+1]
		if abs(ord(a)-ord(b)) == CAP_DIFF:
			react_idx.add(i)
			react_idx.add(i+1)
			skip_one = True  # Don't want to double delete
	new_s = ""
	for i in range(len(s)):
		if i not in react_idx:
			new_s += s[i]
	print("Reaction removed {} items. New string length: ".format(len(react_idx)), len(new_s))
	return new_s

def part1(input):
	prev = ""
	curr = input
	while curr != prev:
		prev = curr
		curr = react(prev)
	return curr
	
print("Reading...")
input = read()
print("Initial length: ", len(input))
print("Part 1: ", part1(input))  # 10766
