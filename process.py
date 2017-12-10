def main():
	print "Part 1: ", part1()

def part1():
	f = open("day9.txt", "r")
	code = f.readlines()
	para = []
	code = code[0]

	count = 0
	gsum = 0
	flag = True
	note = False

	braces = []
	o = 0
	c = 0
	for text in code:
		if text == '<' and not note:
			flag = False
		if text == '>' and not note:
			flag = True
		if text == '{' and flag:
			count += 1
			braces.append('{')
			gsum += count
			o += 1
		if text == '}' and count > 0 and flag:
			count -= 1
			braces.append('}')
			c += 1
		if text == '!' and not note:
			note = True
			continue
		note = False

	return gsum

if __name__ == "__main__":
	main()
