FILENAME = "test.txt"


def part1() -> int:
	total = 0
	with open(FILENAME, "r") as f:
		lines = [list(l.strip("\n")) for l in f.readlines()]

	for lineIndex, line in enumerate(lines):
		for rockIndex, rock in enumerate(line):
			if rock != "O":
				continue
			movingIndex = lineIndex
			canMove = True
			while canMove:
				if movingIndex-1 < 0:
					canMove = False
				elif lines[movingIndex-1][rockIndex] == ".":
					lines[movingIndex-1][rockIndex] = "O"
					lines[movingIndex][rockIndex] = "."
					movingIndex -= 1
				else:
					canMove = False
			total += len(lines) - movingIndex
	return total


def tiltNorth(lines: list[list[str]]) -> None:
	for lineIndex, line in enumerate(lines):
		for rockIndex, rock in enumerate(line):
			if rock != "O":
				continue
			movingIndex = lineIndex
			canMove = True
			while canMove:
				if movingIndex-1 < 0:
					canMove = False
				elif lines[movingIndex-1][rockIndex] == ".":
					lines[movingIndex-1][rockIndex] = "O"
					lines[movingIndex][rockIndex] = "."
					movingIndex -= 1
				else:
					canMove = False


def tiltSouth(lines: list[list[str]]) -> None:
	for lineIndex in range(len(lines)):
		actualIndex = len(lines) - lineIndex - 1
		for rockIndex, rock in enumerate(lines[actualIndex]):
			movingIndex = actualIndex
			if rock != "O":
				continue
			canMove = True
			while canMove:
				if movingIndex + 1 > len(lines) - 1:
					canMove = False
				elif lines[movingIndex+1][rockIndex] == ".":
					lines[movingIndex+1][rockIndex] = "O"
					lines[movingIndex][rockIndex] = "."
					movingIndex += 1
				else:
					canMove = False


def tiltWest(lines: list[list[str]]) -> None: 
	for lineIndex, line in enumerate(lines):
		for rockIndex, rock in enumerate(line):	
			if rock != "O":
				continue
			movingIndex = rockIndex
			canMove = True
			while canMove:
				if movingIndex - 1 < 0:
					canMove = False
				elif lines[lineIndex][movingIndex-1] == ".":
					lines[lineIndex][movingIndex-1] = "O"
					lines[lineIndex][movingIndex] = "."
					movingIndex -= 1
				else:
					canMove = False


def tiltEast(lines: list[list[str]]) -> None:
	for lineIndex, line in enumerate(lines):
		for rockIndex in range(len(line)-1, -1, -1):	
			if line[rockIndex] != "O":
				continue
			movingIndex = rockIndex
			canMove = True
			while canMove:
				if movingIndex + 1 > len(line)-1:
					canMove = False
				elif lines[lineIndex][movingIndex+1] == ".":
					lines[lineIndex][movingIndex+1] = "O"
					lines[lineIndex][movingIndex] = "."
					movingIndex += 1
				else:
					canMove = False


def cycle(lines: list[list[str]]) -> None:
	tiltNorth(lines)
	tiltWest(lines)
	tiltSouth(lines)
	tiltEast(lines)


def getTotal(lines: list[list[str]]) -> int:
	total = 0
	for lineIndex, line in enumerate(lines):
		for rock in line:
			if rock == "O":
				total += len(lines) - lineIndex
	return total


def part2() -> int:
	total = 0
	with open(FILENAME, "r") as f:
		lines = [list(l.strip("\n")) for l in f.readlines()]
	
	for count in range(10000):
		if count % (10000 * (10 / 100)) == 0:
			print(count)
		cycle(lines)
	total = getTotal(lines)
	for line in lines:
		print("".join(line), end="\n")
	return total


if __name__ == '__main__':
	print("========== Part 1 ==========")
	print(f"Part 1 result: {part1()}")
	print("========== Part 2 ==========")
	print(f"Part 2 result: {part2()}")