mx = 0
def main():
	buffer = []
	while 1:
		try:
			line = raw_input()
			buffer.append(line)
		except EOFError:
			break
	print "Part 1: ", part1(buffer)
	print "Part 2: ", mx

def part1(p):
	global mx
	
	varDict = {}
	
	for line in p:
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
