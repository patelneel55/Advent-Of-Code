def main():
	line = raw_input()	
	print "Part 1: ", part1(line)
	print "Part 2: ", part2(line)

def part1(p):

	count = 0
	gsum = 0
	flag = True
	note = False

	braces = []
	o = 0
	c = 0
	for text in p:
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


def part2(p):
	charCount = 0
	garbo = False
	note = False

	for text in p:
		if text == '<' and not note and not garbo:
			garbo = True
			continue
		if text == '>' and not note:
			garbo = False
		if text == '!' and garbo and not note:
			note = True
			continue

		if garbo and not note:
			charCount += 1
		note = False

	return charCount

if __name__ == "__main__":
	main()
