import sys

def read():
	input = []
	for line in sys.stdin:
		i = int(line)
		input.append(i)
	print("Read {} entries".format(len(input)))
	return input

def part1(input):
	sum = 0
	for n in input:
		sum += n
	print("Part 1 answer: {}".format(sum))

def part2(input):
	seen = set({})
	val = 0
	for i in range (1,1000):
		for n in input:
			seen.add(val)
			val += n
			if val in seen:
				print("Part 2 answer: {}".format(val))
				return
		print("Loop {} of input complete.".format(i))

input  = read()
part1(input) # 585
part2(input) # 83173
