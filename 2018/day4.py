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

def ts_min(ts):
	return int(ts[-2:])

def backfill_sleep(hist, guard, start, end):
	for i in range(start, end):
		hist[hist_key(guard, i)] += 1

# return {"guard:minute": count_of_sleeping}
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
			sleep_start = ts_min(key)  # key is minute
		else:
			backfill_sleep(sleeps, current_guard, sleep_start, ts_min(key))
			sleep_start = 60
	backfill_sleep(sleeps, current_guard, sleep_start, 60)
	return sleeps

def sleeps_totals(sleeps):
	totals = defaultdict(int)
	for k, v in sleeps.items():
		g = int(k.split(":")[0])
		totals[g] += v
	return totals

def laziest_guard(totals):
	lazy_g = 0
	for k, v in totals.items():
		if lazy_g == 0 or totals[lazy_g] < v:
			lazy_g = k
	return lazy_g

# Find laziest key matching guard
# Guard = 0  means check across all guards
def laziest(sleeps, guard):
	mk = ""
	mv = 0
	for k, v in sleeps.items():
		if guard != 0:
			tg = int(k.split(":")[0])
			if tg != guard:
				continue;
		if mk == "" or mv < v:
			mk = k
			mv = v
	return mk

def part1(input):
	sleeps = guard_sleeps(input)
	totals = sleeps_totals(sleeps)
	
	lazy_g = laziest_guard(totals)

	key = laziest(sleeps, lazy_g)
	minute = int(key.split(":")[1])
	return lazy_g * minute

def part2(input):
	sleeps = guard_sleeps(input)
	mk = laziest(sleeps, 0)
	g = int(mk.split(":")[0])
	cnt = int(mk.split(":")[1])
	print(g, cnt)
	return g * cnt

print("Reading...")
input = read()
print(part1(input))  # 48680
print(part2(input))  # 94826
