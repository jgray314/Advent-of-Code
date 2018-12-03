import sys

def read():
	return int(sys.stdin.readline())

def last_complete_sqrt(val):
	inner_sqrt = 1
	while (inner_sqrt+2)**2 <= val:
		inner_sqrt +=2
	return inner_sqrt

# distance to walk from center of edge to center of square
def walk_in(val):
	sqrt = last_complete_sqrt(val)
	dist = int(sqrt / 2)
	if val != sqrt**2:
		dist +=1
	return dist

def walk_edge(val):
	sqrt = last_complete_sqrt(val)
	edge_start = sqrt**2
	len_edge_map = sqrt + 1
	while val > edge_start:
		edge_start += len_edge_map
	midpt = edge_start - int(len_edge_map/2)
	return abs(val - midpt)

def manhattan_dist(val):
	if val == 1:
		return 0
	inward = walk_in(val)
	edge = walk_edge(val)
	print("val: {} edge:{} inward: {}".format(val, edge, inward))
	return edge + inward


input = read()
print("Part 1: {}".format(manhattan_dist(input)))  #326
#print("Part 2: {}".format(part2(input)))
