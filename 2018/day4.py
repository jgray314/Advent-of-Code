import sys
from collections import defaultdict
import datetime

SLEEP = "sleep"
WAKE = "wake"

def read():
	input = {}
	for line in sys.stdin:
		br = line.split("]")
		ts = br[0][1:]
		if br[1].startswith(" Guard"):
			input[ts] = int(br[1].split(" ")[2][1:])
		elif br[1].startswith(" falls"):
			input[ts] = SLEEP
		else:
			input[ts] = WAKE
	print("Read {} entries".format(len(input)))
	return input

def hist_key(guard, minute):
	return "{}:{}".format(guard, minute)

def key_guard(k):
	return int(k.split(":")[0])

def backfill_sleep(hist, guard, start, end):
	#print(guard, start, end)
	for i in range(start, end):
		hist[hist_key(guard, i)] += 1

def guard_sleeps(input):
	sleeps = defaultdict(int)
	current_guard = -1
	sleep_start = 60
	for key in sorted(input):
		val = input[key]
		if type(val) is int:
			backfill_sleep(sleeps, current_guard, sleep_start, 60)
			current_guard = val
			sleep_start = 60
		elif val == SLEEP:
			sleep_start = int(key[-2:])  # key is minute
		else:
			backfill_sleep(sleeps, current_guard, sleep_start, int(key[-2:]))
			sleep_start = 60
	backfill_sleep(sleeps, current_guard, sleep_start, 60)
	return sleeps

def sleeps_totals(sleeps):
	totals = defaultdict(int)
	for k, v in sleeps.items():
		g = int(k.split(":")[0])
		totals[g] += v
	return totals

def part1(input):
	sleeps = guard_sleeps(input)
	totals = sleeps_totals(sleeps)
	print(totals)
	
	lazy_g = 0
	for k, v in totals.items():
		if lazy_g == 0 or totals[lazy_g] < v:
			lazy_g = k

	minute = 60
	max = 0
	for k, v in sleeps.items():
		s = k.split(":")
		g = int(s[0])
		m = int(s[1])
		if g != lazy_g:
			continue
		#print(k, v, minute, max, lazy_g)
		if minute == 60 or max < v:
			minute = m
			max = v
	print(lazy_g, minute)
	return lazy_g * minute

def hist_sleep_odds(input):
	sleeps = guard_sleeps(input)
	guard_duty = defaultdict(int)
	for k, v in input.items():
		if type(v) is int:
			guard_duty[v] += 1

	guard_odds = {}
	for k, v in sleeps.items():
		guard_odds[k] = v / guard_duty[key_guard(k)]
	return guard_odds

print("Reading...")
input = read()
print(part1(input))
