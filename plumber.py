def main():
	buffer = []
	while 1:
		try:
			line = raw_input()
			buffer.append(line.strip())
		except EOFError:
			break
	print "Part 1: ", part1(buffer)
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
		
	
if __name__ == "__main__":
	main()
