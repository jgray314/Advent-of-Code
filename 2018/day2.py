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

def char_diff_idxs(s1, s2):
	c_diff = []
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			c_diff.append(i)
	return c_diff

def part2(input):
	print("Starting part2...")
	for l1 in input:
		for l2 in input:
			if l1 == l2:
				continue
			cdi = char_diff_idxs(l1, l2)
			if len(cdi) == 1:
				idx = cdi[0]
				print("{} vs {} at idx {}".format(l1, l2, idx))
				return l1[:idx] + l1[(idx + 1):]

print("Reading input...")
input = read()
print("Part 1 result: {}".format(part1(input)))  # 6642
print("Part 2 result: {}".format(part2(input)))  # cvqlbidheyujgtrswxmckqnap
