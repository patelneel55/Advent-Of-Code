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

	steps = 0
	i = 0
	while 1:
		if(i < 0 or i >= len(f)):
			break
		prev = i
		i += int(f[i])
		f[prev] = int(f[prev]) + 1
		steps += 1
		
	return steps
	
def part2(f):
	file = open("day5.txt", "r")
	list = file.readlines()

	steps = 0
	i = 0
	while 1:
		if(i < 0 or i >= len(list)):
			break
		prev = i
		i += int(list[i])
		if int(list[prev]) >= 3:
			list[prev] = int(list[prev]) - 1
		else:
			list[prev] = int(list[prev]) + 1
		
		steps += 1
		
	return steps
	
if __name__ == "__main__":
	main()
