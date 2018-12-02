import sys

def read():
	str = sys.stdin.readline()
	input = []
	for c in str:
		input.append(int(c))
	return input

def part1(input):
	sum = 0
	for i in range(len(input)):
		if input[i] == input[i-1]:
			sum += input[i]
	return sum

input = read()
print("Part 1: {}".format(part1(input)))  # 1175
