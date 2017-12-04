def main():
	print "Part 1: ", part1()

def part1():
	file = open("pass.txt", "r")
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
	
if __name__ == "__main__":
	main()