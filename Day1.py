import sys

def part1():
	sum = 0
	for line in sys.stdin:
		sum += int(line)
	print(sum)

part1() #585
