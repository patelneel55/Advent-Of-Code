def main():
	list = raw_input()
	print "Part 1: ", part1(list)
	print "Part 2: ", part2(list)

def part1(p):
	list = map(int, p.split())
	its = 0
	length = len(list)
	mx = list[0]
	ind = 0
	test = []
	while 1:
		mx = max(list)
		ind = list.index(max(list))
		i = 0
		if mx >= (length - 1):

			while (mx - i) % (length-1) != 0:
				i += 1

			mx = (mx - i) / (length - 1)
			for m in xrange(length):
				if m != ind:
					list[m] += mx
			list[ind] = i
		else:
			count = 0
			for k in xrange(ind+1, length):
				if count < mx:
					list[k] += 1
					count += 1
			for a in xrange(0, ind + 1):
				if count < mx:
					count += 1
					list[a] += 1
			list[ind] = 0

		its += 1
		sForm = ''.join(map(str, list))
		if(test.count(sForm) > 0):
			break;
		test.append(sForm)
	
	return its

def part2(p):
	list = map(int, p.split())
	its = 0
	length = len(list)
	mx = list[0]
	ind = 0
	test = []
	sForm = ""
	while 1:
		mx = max(list)
		ind = list.index(max(list))
		i = 0
		if mx >= (length - 1):

			while (mx - i) % (length-1) != 0:
				i += 1

			mx = (mx - i) / (length - 1)
			for m in xrange(length):
				if m != ind:
					list[m] += mx
			list[ind] = i
		else:
			count = 0
			for k in xrange(ind+1, length):
				if count < mx:
					list[k] += 1
					count += 1
			for a in xrange(0, ind + 1):
				if count < mx:
					count += 1
					list[a] += 1
			list[ind] = 0

		its += 1
		sForm = ''.join(map(str, list))
		if(test.count(sForm) > 0):
			break;
		test.append(sForm)
	num = len(test) - test.index(sForm)
	return num


if __name__ == "__main__":
	main()
