mx = 0
def main():
	print "Part 1: ", part1()
	print "Part 2: ", mx

def part1():
	global mx
	f = open("day8.txt", "r")
	
	varDict = {}
	
	for line in f:
		comp = line.strip().split()

		if not comp[4] in varDict:
			varDict[comp[4]] = 0
		if not comp[0] in varDict:
			varDict[comp[0]] = 0
		if comp[1] == "inc":
			command = "varDict[comp[0]] += " + comp[2] + " if varDict[comp[4]] " + comp[5] + " " + comp[6] + " else 0"
		else:
			command = "varDict[comp[0]] -= " + comp[2] + " if varDict[comp[4]] " + comp[5] + " " + comp[6] + " else 0"
		eval(compile(command, '<string>', 'exec'))
		if mx < varDict[comp[0]]:
			mx = varDict[comp[0]]

	return max(varDict.values())	
if __name__ == "__main__":
	main()
