def main():
	num = raw_input("Enter the number:")
	print "Part 1: ", part1(num)
	print "Part 2: ", part2(num)


def part1(num):
	total = 0
	for i in range(len(num) - 1):
		if num[i] == num[i+1]:
			total += int(num[i])
	if num[0] == num[len(num) - 1]:
		total += int(num[0])

	return total
	
def part2(num):
	total = 0;
	for i in range(len(num)):
		index = 0;
		if i+(len(num)/2) >= len(num):
			index = i+(len(num)/2) - len(num)
		else:
			index = i+(len(num)/2)
		if num[i] == num[index]:
			total += int(num[i])
	return total

if __name__ == "__main__":
	main()	
