from itertools import count

import math
def main():
	num = input("Enter a number: ")
	print "Part 1: ", part1(num)
	print "Part 2: ", part2(num)

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


def sum_spiral():
    a, i, j = {(0,0) : 1}, 0, 0
    sn = lambda i,j: sum(a.get((k,l), 0) for k in range(i-1,i+2)
                                         for l in range(j-1,j+2))
    for s in count(1, 2):
        for _ in range(s):   i += 1; a[i,j] = sn(i,j); yield a[i,j]
        for _ in range(s):   j -= 1; a[i,j] = sn(i,j); yield a[i,j]
        for _ in range(s+1): i -= 1; a[i,j] = sn(i,j); yield a[i,j]
        for _ in range(s+1): j += 1; a[i,j] = sn(i,j); yield a[i,j]

def part2(num):
	for i in sum_spiral():
		if i > num:
			return i

if __name__ == "__main__":
	main()
