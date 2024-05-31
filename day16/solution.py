FILENAME = "input.txt"


def part1() -> int:
	total = 0
	with open(FILENAME, "r") as f:
		lines = [l.strip("\n") for l in f.readlines()]
	startBeams = [[[-1, x],[1,0]] for x in range(len(lines[0]))] + [[[len(lines), x], [-1,0]] for x in range(len(lines))] + [[[x, -1], [0, 1]] for x in range(len(lines))] + [[[x, len(lines[0])], [0, -1]] for x in range(len(lines))]
	beams = []
	debug = [["." for _ in range(len(lines[1]))] for _ in range(len(lines))]
	# debug[0][0] = "#"
	for index, startBeam in enumerate(startBeams):
		print(len(startBeams), ": ", index+1)
		beams = [startBeam]
		energized = []
		for beam in beams:
			been = []
			active = True
			currentPos = [beam[0][0], beam[0][1]]
			direction = [beam[1][0], beam[1][1]]
			while active:
				currentPos[0] += direction[0]
				currentPos[1] += direction[1]
				if [currentPos, direction] in been:
					break
				been.append([[currentPos[0], currentPos[1]], [direction[0], direction[1]]])
				if currentPos[0] < 0 or currentPos[0] >= len(lines) or currentPos[1] < 0 or currentPos[1] >= len(lines[0]):
					break
				elif currentPos not in energized:
					energized.append([currentPos[0], currentPos[1]])
					# debug[currentPos[0]][currentPos[1]] = "#"
				match lines[currentPos[0]][currentPos[1]]:
					case "/":
						# debug[currentPos[0]][currentPos[1]] = "/"
						if direction[1] == 1:
							direction = [-1, 0]
						elif direction[1] == -1:
							direction = [1, 0]
						elif direction[0] == 1:
							direction = [0, -1]
						elif direction[0] == -1:
							direction = [0, 1]
					case "\\":
						# debug[currentPos[0]][currentPos[1]] = "\\"
						if direction[1] == 1:
							direction = [1, 0]
						elif direction[1] == -1:
							direction = [-1, 0]
						elif direction[0] == 1:
							direction = [0, 1]
						elif direction[0] == -1:
							direction = [0, -1]
					case "-":
						# debug[currentPos[0]][currentPos[1]] = "-"
						if direction[0] in [-1, 1]:
							direction = [0, -1]
							if [[currentPos[0], currentPos[1]], [0, 1]] not in beams: 
								beams.append([[currentPos[0], currentPos[1]], [0, 1]])
					case "|":
						# debug[currentPos[0]][currentPos[1]] = "|"
						if direction[1] in [-1, 1]:
							direction = [-1, 0]
							if [[currentPos[0], currentPos[1]], [1, 0]] not in beams:
								beams.append([[currentPos[0], currentPos[1]], [1, 0]])
		total = max(total, len(energized))
	# for line in debug:
		# print("".join(line), end="\n")
	# print("\n")
	return total


if __name__ == '__main__':
	print("========== Part 1 ==========")
	print(f"Part 1 result: {part1()}")
	# print("========== Part 2 ==========")
	# print(f"Part 2 result: {part2()}")	