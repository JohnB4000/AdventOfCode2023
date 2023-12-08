FILENAME = "input.txt"
CARD_ORDER = {
	"A": 1,
	"K": 2,
	"Q": 3,
	"J": 4,
	"T": 5,
	"9": 6,
	"8": 7, 
	"7": 8, 
	"6": 9, 
	"5": 10, 
	"4": 11, 
	"3": 12, 
	"2": 13,
	"J": 14
}


def getMaxIndex(array: list[int]) -> int:
	if array == []:
		return -1
	max = array[0]
	index = 0
	for x in range(1, len(array)):
		if array[x] > max:
			max = array[x]
			index = x
	return index


def countOccurances(line: list[str]) -> list[int]:
	jacks = 0
	occurances = {}
	for card in line:
		if card == "J":
			jacks += 1
		elif card in occurances:
			occurances[card] += 1
		else:
			occurances[card] = 1
	totalOccurances = [occurances[key] for key in occurances]
	if jacks > 0:
		maxIndex = getMaxIndex(totalOccurances)
		if maxIndex != -1:
			totalOccurances[maxIndex] += jacks
		else:
			totalOccurances.append(5)
	return totalOccurances


def contains(array: list[int], num: int):
	for element in array:
		if num == element:
			return True
	return False 


def compare(card1, card2):
	for index in range(5):
		if CARD_ORDER[card1[0][index]] > CARD_ORDER[card2[0][index]]:
			return True
		elif CARD_ORDER[card1[0][index]] < CARD_ORDER[card2[0][index]]:
			return False
	return False


def sortType(type: list[list[str]]) -> list[list[str]]:
	swaps = True
	n = 1
	while (swaps):
		swaps = False
		for index in range(len(type) - n):
			if compare(type[index], type[index+1]):
				temp = type[index]
				type[index] = type[index+1]
				type[index+1] = temp
				swaps = True
		n += 1


def rankTypes(lines: list[list[str]]) -> list[list[str]]:
	types = [[], [], [], [], [], [], []]
	sortedTypes = []
	for line in lines:
		if contains(countOccurances(line[0]), 5):
			types[0].append(line)
		elif contains(countOccurances(line[0]), 4):
			types[1].append(line)
		elif countOccurances(line[0]) in [[2, 3], [3, 2]]:
			types[2].append(line)
		elif contains(countOccurances(line[0]), 3):
			types[3].append(line)
		elif countOccurances(line[0]) in [[2, 2, 1], [2, 1, 2], [1, 2, 2]]:
			types[4].append(line)
		elif contains(countOccurances(line[0]), 2):
			types[5].append(line)
		else:
			types[6].append(line)
	for type in types:
		sortType(type)
		sortedTypes.extend(type)
	return sortedTypes

def part1() -> int:
	total = 0
	lines = []
	with open(FILENAME, "r") as f:
		lines = [l.strip("\n").split(" ") for l in f.readlines()]
	
	cards = rankTypes(lines)
	for index, card in enumerate(cards):
		total += int(card[1]) * (len(cards) - index)
	return total


if __name__ == '__main__':
	print("========== Part 1 ==========")
	print(f"Part 2 result: {part1()}")
	# print("========== Part 2 ==========")
	# print(f"Part 2 result: {part2()}")