FILENAME = "input.txt"


def notAllZeros(array: list[int]) -> bool:
	notAllZeros = False
	for num in array:
		if num != 0:
			notAllZeros = True
	return notAllZeros


def part1() -> int:
	total = 0
	second = 0
	lines = []
	with open(FILENAME, "r") as f:
		lines = [l.strip("\n") for l in f.readlines()]

	for line in lines:
		line = [int(num) for num in line.split(" ")]
		differences = [line]
		differenceIndex = 0
		while (notAllZeros(differences[differenceIndex])):
			currentDifferences = []
			for index in range(len(differences[differenceIndex]) - 1):
				currentDifferences.append(differences[differenceIndex][index+1] - differences[differenceIndex][index])
			differences.append(currentDifferences)
			differenceIndex += 1
		
		copy = differenceIndex
		differences[differenceIndex].append(0)
		for _ in range(1, len(differences)):
			differenceIndex -= 1
			differences[differenceIndex].append(differences[differenceIndex][-1] + differences[differenceIndex+1][-1])
		total += differences[0][-1]
		
		differenceIndex = copy
		differences[differenceIndex].append(0)
		for _ in range(1, len(differences)):
			differenceIndex -= 1
			differences[differenceIndex].insert(0, differences[differenceIndex][0] - differences[differenceIndex+1][0])
		second += differences[0][0]
	return total, second


if __name__ == '__main__':
	print("========== Part 1 ==========")
	print(f"Part 1 result: {part1()}")
	# print("========== Part 2 ==========")
	# print(f"Part 2 result: {part2()}")