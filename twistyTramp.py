def main():
	print "Part 1: ", part1()
	print "Part 2: ", part2()
	
def part1():
	file = open("twisty.txt", "r")
	list = file.readlines()
	
	steps = 0
	i = 0
	while 1:
		if(i < 0 or i >= len(list)):
			break
		prev = i
		i += int(list[i])
		list[prev] = int(list[prev]) + 1
		steps += 1
		
	return steps
	
def part2():
	file = open("twisty.txt", "r")
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
