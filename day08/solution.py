import math


FILENAME = "input.txt"


def followInstructionIndex(currentNode: str, instruction: str, nodes: list[dict[str,str]]) -> str:
	nextPathIndex = -1
	match instruction:
		case "L":
			nextPathIndex = 0
		case "R":
			nextPathIndex = 1

	for index, node in enumerate(nodes):
		if node["currentNode"] == currentNode:
			return node["options"][nextPathIndex]
	print("failed")
	return ""


def part1() -> int:
	steps = 0
	lines = []
	with open(FILENAME, "r") as f:
		lines = [l.strip("\n") for l in f.readlines()]

	instructions = lines[0]
	nodes = []
	for line in lines[2:]:
		node = {
			"currentNode": line[0:3],
			"options": [line[7:10], line[12:15]],
		}
		nodes.append(node)

	currentNode = "AAA"
	instructionIndex = 0
	
	while (currentNode != "ZZZ"):
		currentNode = followInstructionIndex(currentNode, instructions[instructionIndex], nodes)
		steps += 1
		instructionIndex += 1
		if instructionIndex >= len(instructions):
			instructionIndex = 0
	return steps


def nodeFinished(currentNodes: str):
	if currentNodes[2] == "Z":
		return True
	return False


def part2() -> int:
	lines = []
	with open(FILENAME, "r") as f:
		lines = [l.strip("\n") for l in f.readlines()]

	instructions = lines[0]
	nodes = []
	for line in lines[2:]:
		node = {
			"currentNode": line[0:3],
			"options": [line[7:10], line[12:15]],
		}
		nodes.append(node)

	currentNodes = [node["currentNode"] for node in nodes if node["currentNode"][2] == "A"]
	stepsRecord = []
	steps = 0
	instructionIndex = 0
	while (currentNodes != []):
		for index, node in enumerate(currentNodes):
			currentNodes[index] = followInstructionIndex(node, instructions[instructionIndex], nodes)
		instructionIndex += 1
		steps += 1
		if instructionIndex >= len(instructions):
			instructionIndex = 0
		for node in currentNodes:
			if nodeFinished(node):
				stepsRecord.append(steps)
				currentNodes.remove(node)
	return math.lcm(*stepsRecord)


if __name__ == '__main__':
	print("========== Part 1 ==========")
	print(f"Part 1 result: {part1()}")
	print("========== Part 2 ==========")
	print(f"Part 2 result: {part2()}")