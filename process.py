def main():
	part1()

def part1():
	f = open("day9.txt", "r")
	code = f.readlines()
	para = []
	code = code[0]

	for char in code:
		if char == '}' or char == '{' or char == '!' or char == '<' or char == '>':
			para.append(char)
	print code
	print para

	count = 0
	gsum = 0
	flag = True
	note = False

	for text in para:
		if text == '<' and not note:
			flag = False
		if text == '>' and not note:
			flag = True
		if text == '{' and flag:
			count += 1
			gsum += count
		if text == '}' and flag:
			count -= 1
		if text == '!' and not note:
			note = True
			continue
		if note:
			note = False
	print gsum

if __name__ == "__main__":
	main()
