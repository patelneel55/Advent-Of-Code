def main():
	buffer = []
	while 1:
		try:
			line = raw_input()
			buffer.append(line.strip())
		except EOFError:
			break
	print "Part 1: ", part1(buffer)
	print "Part 2: ", part2(buffer)
def part1(line):
	zeroCon = []

	while 1:
		num = len(zeroCon)
		for p in line:
			comp = p.split(" <-> ")
			child = comp[1].split(", ")

			if comp[0] == '0':
				for i in child:
					if not i in zeroCon:	
						zeroCon.append(i)
			else:
				for i in child:
					if i in zeroCon and not comp[0] in zeroCon:
						zeroCon.append(comp[0])
		if num == len(zeroCon):
			break
	return len(zeroCon) + 1

def part2(lines):	
	adjlist = {}
	for line in lines:
		splitline = line.split(' <-> ')
		dest = splitline[1].split(', ')
		destint = [int(a) for a in dest]
		adjlist[int(splitline[0])] = destint

	counter = 0
	found = {}
	for key in adjlist:
		if key not in found:
			counter += 1
			q =	[key]
			while len(q) > 0:
				a = q.pop(0)
				if a not in found:
					found[a] = 1
					for elem in adjlist[a]:
						q.append(elem)
	return counter
		
	
if __name__ == "__main__":
	main()
