FILENAME = "input.txt"


def expandSpace(lines: list[str]) -> list[str]:
	expandedSpace = []
	for line in lines:
		expandedSpace.append(line)
		if line == "." * len(line):
			for x in range(1_000_000):
				expandedSpace.append(line)
	expandedSpaceVertical = ['' for x in range(len(expandedSpace))]
	for index in range(len(expandedSpace[0])):
		empty = True
		for lineIndex in range(len(expandedSpace)):
			expandedSpaceVertical[lineIndex] += expandedSpace[lineIndex][index]
			if expandedSpace[lineIndex][index] == '#':
				empty = False
		if empty:
			for _ in range(1_000_000):
				for x in range(len(expandedSpace)):
					expandedSpaceVertical[x] += '.'
	return expandedSpaceVertical


def findGalaxies(lines: list[str]) -> list[tuple[int, int]]:
	galaxies = []
	for x in range(len(lines)):
		for y in range(len(lines[x])):
			if lines[x][y] == '#':
				galaxies.append((x,y))
	return galaxies


def getDistances(galaxies: list[tuple[int, int]]) -> int:
	total = 0
	for index, galaxy in enumerate(galaxies):
		for otherGalaxy in galaxies[index:]:
			total += abs(galaxy[0] - otherGalaxy[0]) + abs(galaxy[1] - otherGalaxy[1])
	return total

def part1() -> int:
	total = 0
	lines = []
	with open(FILENAME, "r") as f:
		lines = [l.strip("\n") for l in f.readlines()]
	lines = expandSpace(lines)
	print("Expanded Space")
	galaxies = findGalaxies(lines)
	print("Counted Galxies")
	total = getDistances(galaxies)

	return total

if __name__ == '__main__':
	print("========== Part 1 ==========")
	print(f"Part 1 result: {part1()}")
	# print("========== Part 2 ==========")
	# print(f"Part 2 result: {part2()}")