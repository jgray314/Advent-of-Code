import sys
from collections import defaultdict

def read():
	input = {}
	for line in sys.stdin:
		ca = line.split(" ")
		id = int(ca[0][1:])
		xy = ca[2][:-1].split(",")
		wh = ca[3][:-1].split("x")
		data = {
			'x': int(xy[0]),
			'y': int(xy[1]),
			'width': int(wh[0]),
			'height':  int(wh[1])
		}
		input[id] = data
	print("Read {} entries".format(len(input)))
	return input

def idx(x, y):
	return x * 1000 + y

def get_fabric_overlay(input):
	fabric = defaultdict(list)
	for k, v in input.items():
		for dx in range(v['width']):
			for dy in range(v['height']):
				fabric[idx(v['x']+dx, v['y']+dy)].append(k)
	return fabric

def part1(fabric):
	sum = 0
	for k, v in fabric.items():
		if len(v) > 1:
			sum += 1
	return sum

def part2(fabric):
	max_overlap = defaultdict(int)
	for k, v in fabric.items():
		overlap = len(v)
		for item in v:
			if max_overlap[item] < overlap:
				max_overlap[item] = overlap
	for k, v in max_overlap.items():
		if v == 1:
			return k
	return 0

input = read()
fabric = get_fabric_overlay(input)
print("Part 1: {}".format(part1(fabric)))  # 103806
print("Part 2: {}".format(part2(fabric)))  # 625
