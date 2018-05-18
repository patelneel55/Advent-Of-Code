from string import ascii_lowercase
def main():
	buffer = []
	while 1:
		try:
			line = raw_input()
			buffer.append(line)
		except EOFError:
			break
	part1(buffer)

def part1(instruct):

	for i in xrange(len(instruct)):
		instruct[i] = instruct[i].strip().split()
	print instruct
	reg = {}
	for c in ascii_lowercase:
		if c == 'i':
			break;
		reg[c] = 0
	
	i = 0
	count = 0
	while i < len(instruct):
		action = instruct[i][0]
		regt = instruct[i][1]
		val = instruct[i][2]
		if action == "set":
			if val in reg:
				reg[regt] = reg[val]
			else:
				reg[regt] = int(val)

		if action == "mul":
			count += 1
			if val in reg:
				reg[regt] = int(reg[regt]) * int(reg[val])
			else:
				reg[regt] = int(reg[regt]) * int(val)

		if action == "sub":
			if val in reg:
				reg[regt] = int(reg[regt]) - int(reg[val])
			else:
				reg[regt] = int(reg[regt]) - int(val)
		i += 1

	print reg

if __name__ == "__main__":
	main()
