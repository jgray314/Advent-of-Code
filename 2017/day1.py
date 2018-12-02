import sys

def read():
	str = sys.stdin.readline()
	input = []
	for c in str:
		input.append(int(c))
	return input

def compare_idx_rot(input, diff):
	sum = 0
	for i in range(len(input)):
		if input[i] == input[i+diff]:
			sum += input[i]
	return sum

def part1(input):
	return compare_idx_rot(input, -1)

def part2(input):
	rot = int(len(input) / -2)
	return compare_idx_rot(input, rot)
	
input = read()
print("Part 1: {}".format(part1(input)))
print("Part 2: {}".format(part2(input)))
