FILENAME = "input.txt"


def interpretMap(value: int, map: list[list[int]]) -> int:
	for line in map:
		if value >= line[1] and value <= (line[1] + line[2]):
			return line[0] + (value - line[1])
	return value


def findMin(array: list[int]) -> int:
	min = array[0]
	for ele in array[1:]:
		if ele < min:
			min = ele
	return min


def part1() -> int:
	seeds = []
	maps = []
	with open(FILENAME, "r") as f:
		lines = [l.strip("\n") for l in f.readlines()]
	
	seeds = [int(line) for line in lines[0].split(" ")[1:]]
	
	index = 1
	while index < len(lines):
		index += 2;
		currentMap = []
		while lines[index] != "":
			currentMap.append([int(line) for line in lines[index].split(" ")])
			index += 1
			if index >= len(lines): break
		maps.append(currentMap)

	results = []
	for seed in seeds:
		result = seed
		for map in maps:
			result = interpretMap(result, map)
			print(result)
		results.append(result)
		
	minSeed = findMin(results)
	return minSeed

# def part2() -> int:
# 	seeds = []
# 	maps = []
# 	with open(FILENAME, "r") as f:
# 		lines = [l.strip("\n") for l in f.readlines()]
	
# 	seedRanges = [int(line) for line in lines[0].split(" ")[1:]]
# 	seeds = []
	
# 	for index in range(0, len(seedRanges), 2):
# 		seeds.extend([seed for seed in range(seedRanges[index], seedRanges[index] + seedRanges[index+1])])
	
# 	index = 1
# 	while index < len(lines):
# 		index += 2;
# 		currentMap = []
# 		while lines[index] != "":
# 			currentMap.append([int(line) for line in lines[index].split(" ")])
# 			index += 1
# 			if index >= len(lines): break
# 		maps.append(currentMap)

# 	results = []
# 	for seed in seeds:
# 		result = seed
# 		for map in maps:
# 			result = interpretMap(result, map)
# 		results.append(result)
		
# 	minSeed = findMin(results)
# 	return minSeed

def part2() -> int:
	seeds = []
	maps = []
	with open(FILENAME, "r") as f:
		lines = [l.strip("\n") for l in f.readlines()]

	index = 1
	while index < len(lines):
		index += 2
		currentMap = []
		while lines[index] != "":
			currentMap.append([int(line) for line in lines[index].split(" ")])
			index += 1
			if index >= len(lines): break
		maps.append(currentMap)
	
	results = []
	
	seedRanges = [int(line) for line in lines[0].split(" ")[1:]]

	for index in range(0, len(seedRanges), 2):
		for seed in range(seedRanges[index], seedRanges[index] + seedRanges[index+1]):
			result = seed
			for map in maps:
				result = interpretMap(result, map)
			results.append(result)
			results = [findMin(results)]
		print(f"{index} finished")
		
	minSeed = findMin(results)
	return minSeed


if __name__ == '__main__':
	print("========== Part 1 ==========")
	print(f"Part 1 result: {part1()}")
	print("========== Part 2 ==========")
	print(f"Part 2 result: {part2()}")