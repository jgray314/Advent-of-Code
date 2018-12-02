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
	min = ai[0]
	max = ai[0]
	for v in ai:
		if v < min:
			min = v
		if v > max:
			max = v
	return max - min

def part1(input):
	checksum = 0
	for ai in input:
		checksum += max_diff(ai)
	return checksum

def even_div_result(ai):
	for v1 in ai:
		for v2 in ai:
			if v1 == v2 or (v1 % v2 != 0 and v2 % v1 != 0):
				continue
			if v1 > v2:
				return int(v1 / v2)
			else:
				return int(v2 / v1)
	return 0
	
def part2(input):
	sum = 0
	for ai in input:
		sum += even_div_result(ai)
	return sum
input = read()
print("Part 1: {}".format(part1(input)))  # 21845
print("Part 2: {}".format(part2(input)))  # 191
