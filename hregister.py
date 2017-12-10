import operator

def main():
	print "Part 1: ", part1()

def part1():
	f = open("day8.txt", "r")
	
	varDict = {}

	for line in f:
		comp = line.strip().split(" ")
		if comp[1] == "inc":
			comp[1] = "+"
		else:
			comp[1] = "-"

		if not comp[4] in varDict:
			varDict[comp[4]] = 0
		if not comp[0] in varDict:
			varDict[comp[0]] = 0

		if comp[5] == ">=":
			if varDict[comp[4]] >= int(comp[6]):
				if comp[1] == "+":
					varDict[comp[0]] += int(comp[2])
				else:
					varDict[comp[0]] -= int(comp[2])
		

		if comp[5] == ">":
			if varDict[comp[4]] > int(comp[6]):
				if comp[1] == "+":
					varDict[comp[0]] += int(comp[2])
				else:
					varDict[comp[0]] -= int(comp[2])


		if comp[5] == "<=":
			if varDict[comp[4]] <= int(comp[6]):
				if comp[1] == "+":
					varDict[comp[0]] += int(comp[2])
				else:
					varDict[comp[0]] -= int(comp[2])

		if comp[5] == "<":
			if varDict[comp[4]] < int(comp[6]):
				if comp[1] == "+":
					varDict[comp[0]] += int(comp[2])
				else:
					varDict[comp[0]] -= int(comp[2])

		if comp[5] == "==":
			if varDict[comp[4]] == int(comp[6]):
				if comp[1] == "+":
					varDict[comp[0]] += int(comp[2])
				else:
					varDict[comp[0]] -= int(comp[2])

		if comp[5] == "!=":
			if varDict[comp[4]] != int(comp[6]):
				if comp[1] == "+":
					varDict[comp[0]] += int(comp[2])
				else:
					varDict[comp[0]] -= int(comp[2])


	lst = sorted(varDict.values(), key=int, reverse=True)
	return lst[0]

if __name__ == "__main__":
	main()
