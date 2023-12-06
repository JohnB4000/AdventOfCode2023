FILENAME = "input.txt"


def findRange(time: int, distance: int) -> int:
	firstTime = 0
	lastTime = 0
	for timeHeld in range(1, time):
		if timeHeld * (time-timeHeld) > distance:
			firstTime = timeHeld
			break
	for timeHeld in range(time, 1, -1):
		if timeHeld * (time-timeHeld) > distance:
			lastTime = timeHeld
			break
	return lastTime - firstTime + 1


def part1() -> int:
	total = 1
	lines = []
	with open(FILENAME, "r") as f:
		lines = [l.strip("\n").split(" ") for l in f.readlines()]
	
	times = []
	for time in lines[0]:
		try:
			times.append(int(time))
		except:
			pass
	
	distances = []
	for distance in lines[1]:
		try:
			distances.append(int(distance))
		except:
			pass
	
	for index in range(len(distances)):
		currentCombinations = findRange(times[index], distances[index])
		if total == 1:
			total = currentCombinations
		else:
			total *= currentCombinations if currentCombinations > 0 else 1

	return total


def part2() -> int:
	lines = []
	with open(FILENAME, "r") as f:
		lines = [l.strip("\n").split(" ") for l in f.readlines()]
	
	times = []
	for time in lines[0]:
		try:
			times.append(int(time))
		except:
			pass
	time = int("".join([str(t) for t in times]))
	
	distances = []
	for distance in lines[1]:
		try:
			distances.append(int(distance))
		except:
			pass
	distance = int("".join([str(d) for d in distances]))
	
	return findRange(time, distance)


if __name__ == '__main__':
	print("========== Part 1 ==========")
	print(f"Part 1 result: {part1()}")
	print("========== Part 2 ==========")
	print(f"Part 2 result: {part2()}")