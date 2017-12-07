def main():
	print "Part 1: ", part1()
	print "Part 2: ", part2()

def part1():
	f = open("day7.txt", "r")
	treeDict = {}

	for line in f:

		# Splits the string into parent and child list
		tree = line.split(" -> ")
		child = []
		if len(tree) == 1:
			continue

		# Extract weight from the list
		tree[0] = tree[0].split()[0]
		child = tree[1].split(", ")
		for i in xrange(len(child)):
			child[i] = child[i].strip("\r\n")
		tree[1] = child
		treeDict[tree[0]] = tree[1]

	toDel = []
	while len(treeDict) != 1:
		for k in treeDict:
			for m in xrange(len(treeDict[k])):
				if treeDict[k][m] in treeDict:
					key = treeDict[k][m]
					treeDict[k][m] = treeDict[key]
					toDel.append(key)
		for s in toDel:
			del treeDict[s]

	for m in treeDict:
		return m

def part2():
	f = open("day7.txt", "r")
	treeDict = {}
	weightDict = {}
	
	for line in f:

		# Splits the string into parent and child list
		tree = line.split(" -> ")
		child = []
		if len(tree) == 1:
			wght = tree[0].split()
			wght[1] = wght[1].strip("()")
			print wght
			continue

		# Extract weight from the list
		tree[0] = tree[0].split()[0]
		child = tree[1].split(", ")
		for i in xrange(len(child)):
			child[i] = child[i].strip("\r\n")
		tree[1] = child
		treeDict[tree[0]] = tree[1]

	toDel = []
	while len(treeDict) != 1:
		for k in treeDict:
			for m in xrange(len(treeDict[k])):
				if treeDict[k][m] in treeDict:
					key = treeDict[k][m]
					treeDict[k][m] = treeDict[key]
					toDel.append(key)
		for s in toDel:
			del treeDict[s]

	print treeDict
		



if __name__ == "__main__":
	main()
