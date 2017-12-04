import math
def main():
	num = input("Enter a number: ")
	print "Part 1: ", part1(num)



def part1(num):
	i = 0
	while num > (i ** 2):
		i += 1
	
	initLength = i / 2;

	sq = i**2
	diff = sq - num
	if diff < i:
		avg = (sq + (sq - i + 1)) / 2
		return initLength + abs(num - avg)
	else:
		ran = (sq - i + 1)
		avg = (ran + (ran - i + 1)) / 2
		return initLength + abs(num - avg)

if __name__ == "__main__":
	main()
