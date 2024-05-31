FILENAME = "input.txt"


def hash(chars: str) -> int:
	value = 0
	for char in chars:
		value += ord(char)
		value *= 17
		value = value % 256
	return value


def part1() -> int:
	total = 0
	lines = []
	with open(FILENAME, "r") as f:
		lines = f.readline().strip("\n")
	lines = lines.split(',')
	for line in lines:
		total += hash(line)
	return total

def part2() -> int:
	hashmap = [[] for _ in range(256)]
	total = 0
	with open(FILENAME, "r") as f:
		lines = f.readline().strip("\n")
	lines = lines.split(',')
	for line in lines:
		opIndex = line.find("-") if line.find("-") != -1 else line.find("=")
		boxIndex = hash(line[:opIndex])
		match (line[opIndex]):
			case "=":
				changed = False
				for lens in hashmap[boxIndex]:
					if lens[0] == line[:opIndex]:
						lens[1] = line[opIndex+1:]
						changed = True
				if not changed:
					hashmap[boxIndex].append([line[:opIndex], line[opIndex+1:]])
			case "-":
				for lens in hashmap[boxIndex]:
					if lens[0] == line[:opIndex]:
						hashmap[boxIndex].remove(lens)
	print(hashmap)
	for boxIndex, box in enumerate(hashmap):
		for	lensIndex, lens in enumerate(box):
			total += (boxIndex+1) * (lensIndex+1) * int(lens[1])
			print((boxIndex+1) * (lensIndex+1) * int(lens[1]))


	return total

if __name__ == '__main__':
	print("========== Part 1 ==========")
	print(f"Part 1 result: {part1()}")
	print("========== Part 2 ==========")
	print(f"Part 2 result: {part2()}")