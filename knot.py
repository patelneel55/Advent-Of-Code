def main():
	line = raw_input()
	print "Part 1: ", part1(line)

def part1(p):
	line = p.strip().split(",")
	
	aryList = []
	count = 0
	skip = 0
	for i in xrange(256):
		aryList.append(i)
	for num in line:
		temp = []
		ct = count
		for i in xrange(int(num)):
			temp.append(aryList[count])
			count += 1
			if count >= len(aryList):
				count = 0
		if (count+skip) >= len(aryList):
			count = (count+skip) - len(aryList)
		else:
			count += skip
		skip += 1
		temp.reverse()
		for i in xrange(int(num)):
			aryList[ct] = temp[i]
			ct += 1
			if ct >= len(aryList):
				ct = 0
	
	return aryList[0]*aryList[1]
		

if __name__ == "__main__":
	main()
