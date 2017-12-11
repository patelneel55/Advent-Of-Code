def main():
	buffer = []
	while 1:
		try:
			line = raw_input()
			buffer.append(line)
		except EOFError:
			break
	print "Part 1: ", part1(buffer)
	print "Part 2: ", part2(buffer)

def part1(f):
	list = []
	num = 0
	flag = True
	for line in f:
		flag = True
		list = []
		words = line.split()
		for i in xrange(len(words)):
			if words[i].strip("\n") not in list:
				list.append(words[i])
			else:
				flag = False
		if flag == True:
			num += 1
	return num
	
def part2(f):
	list = []
	num = 0
	flag = True
	for line in f:
		flag = True
		list = []
		words = line.split()
		for i in xrange(len(words)):
			words[i] = ''.join(sorted(words[i]))
		dup = []
		for x in words:
			if x not in dup:
				dup.append(x)
			else:
				flag = False
		if flag:
			num += 1
	return num
	
if __name__ == "__main__":
	main()
