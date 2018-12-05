import sys
from collections import defaultdict

CAP_DIFF = 32
LETTERS = "abcdefghijklmnopqrstuvwxyz"

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
	#print("Reaction removed {} items. New string length: ".format(len(react_idx)), new_s)
	return new_s

def fully_react(s):
	prev = ""
	curr = s
	while curr != prev:
		prev = curr
		curr = react(prev)
	return curr

def part1(input):
	return len(fully_react(input))

def letter_strip(s, rm):
	new_s = ""
	for c in s:
		if c != rm.lower() and c != rm.upper():
			new_s += c
	return new_s


def part2(input):
	letter_reacts = {}
	for c in LETTERS:
		c_init = letter_strip(input, c)
		letter_reacts[c] = len(fully_react(c_init))
	print(letter_reacts)
	min = len(input)
	for k, v in letter_reacts.items():
		if v < min:
			min = v
	return min

	
print("Reading...")
input = read()
print("Initial length: ", len(input))
print("Part 1: ", part1(input))  # 10766
print("Part 2: ", part2(input))  # 6538
