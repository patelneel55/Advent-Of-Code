import math

def main():
	part1()

def part1():
	line = raw_input()
	line = line.strip().split(",")

	highest = 0
	x = 0
	y = 0
	for command in line:
		if command[0] == 's':
			y -= 1
		else:
			y += 1

		if command[-1] == 'e':
			x += 1
		elif command[-1] == 'w':
			x -= 1
		steps = max(abs(x), abs(y))
		if steps > highest:
			highest = steps

	print "Part 1: ", steps
	print "Part 2: ", highest

if __name__ == "__main__":
	main()
