import math
def main():
	num = input("Enter a number: ")
	print "Part 1: ", part1(num)

def part1(num):
	i = 0
	while num > (i ** 2):
		i += 1

	sq = i**2
	diff = sq - num
	if diff < i:
		avg = (2 * sq - i + 1) / 2
		return (i / 2) + abs(num - avg)
	else:
		avg = (2 * sq - 3 * i + 3) / 2
		return (i / 2) + abs(num - avg)

if __name__ == "__main__":
	main()
