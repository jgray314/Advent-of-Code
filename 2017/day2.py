import sys

def read():
	input = []
	for line in sys.stdin:
		iline = list(map(int, line.split('\t')))
		input.append(iline)
	return input

def max_diff(ai):
	if len(ai) == 0:
		return 0;
	min = int(ai[0])
	max = int(ai[0])
	for v in ai:
		iv = int(v)
		if iv < min:
			min = iv
		if iv > max:
			max = iv
	return max - min

def part1(input):
	checksum = 0
	for ai in input:
		checksum += max_diff(ai)
	return checksum

input = read()
print("Part 1: {}".format(part1(input)))  # 21845 
#print("Part 2: {}".format(part2(input)))
