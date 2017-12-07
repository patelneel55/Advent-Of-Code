def main():
	print "Part 1: ", part1()
	print "Part 2: ", part2()

def part1():
	file = open("day4.txt", "r")
	list = []
	num = 0
	flag = True
	for line in file:
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
	file.close()
	return num
	
def part2():
	file = open("day4.txt", "r")
	list = []
	num = 0
	flag = True
	for line in file:
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
	file.close()
	return num
	
if __name__ == "__main__":
	main()
