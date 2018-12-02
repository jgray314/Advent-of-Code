import sys
from collections import defaultdict

def read():
	input = []
	for line in sys.stdin:
		input.append(line.strip())
	print("Read {} entries".format(len(input)))
	return input

def repeat_cnt_hist(line):
	char_hist = defaultdict(int)
	for c in line:
		char_hist[c] += 1
	cnt_hist = defaultdict(int)
	for k, v in char_hist.items():
		cnt_hist[v] += 1
	return cnt_hist

def part1(input):
	cnt2 = 0
	cnt3 = 0
	for line in input:
		cnt_hist = repeat_cnt_hist(line)
		#print("{} -> {}".format(line.strip(), cnt_hist))
		if cnt_hist[2] > 0:
			cnt2 += 1
		if cnt_hist[3] > 0:
			cnt3 += 1
	return cnt2 * cnt3

print("Reading input...")
input = read()
print("Part 1 result: {}".format(part1(input)))  # 6642
