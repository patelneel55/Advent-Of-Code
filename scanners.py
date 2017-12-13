def main():
	buffer = []
	while 1:
		try:
			line = raw_input()
			buffer.append(line)
		except EOFError:
			break
	print "Part 1: ", part1(buffer)
def part1(lines):
	layers = []

	for line in lines:
		comp = line.strip().split(": ")
		layers.append([int(a) for a in comp])
	
	aDict = {}
	mx = 0
	for p in layers:
		aDict[p[0]] = p[1]
		mx = p[0]
	
	delay = 0
	s = 1300
	while s > 0:
		s = 0
		for i in xrange(mx + 1):
			if i in aDict:
				path = aDict[i] * 2 - 2
				if (i + delay) % path == 0:
					s += 1
		delay += 1
	return delay - 1

if __name__ == "__main__":
	main()
