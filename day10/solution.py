FILENAME = "input.txt"


def getStartPosition(lines: list[str]) -> tuple[int,int]:
	for y in range(len(lines)):
		for x in range(len(lines[y])):
			if lines[y][x] == 'S':
				return y, x
	return -1,-1


def followPath(lines, x, y, newX, newY):
	length = 0
	while lines[newY][newX] != 'S':
		length += 1
		tempX = newX
		tempY = newY
		match lines[newY][newX]:
			case 'S':
				if length > 1:
					return True, length
			case '.':
				return False, -1
			case '-':
				if x != newX + 1 or y != newY:
					newX += 1
				else: 
					newX -= 1
			case '|':
				if x != newX or y != newY + 1: 
					newY += 1
				else:
					newY -= 1
			case 'F':
				if x != newX + 1 or y != newY:
					newX += 1
				else:
					newY += 1
			case 'L':
				if x != newX + 1 or y != newY:
					newX += 1
				else:
					newY -= 1
			case 'J':
				if x != newX - 1 or y != newY:
					newX -= 1
				else:
					newY -= 1
			case '7':
				if x != newX - 1 or y != newY:
					newX -= 1
				else:
					newY += 1
		x = tempX
		y = tempY
	return True, length+1

def part1() -> int:
	lines = []
	with open(FILENAME, "r") as f:
		lines = [l.strip("\n") for l in f.readlines()]

	y, x = getStartPosition(lines)

	for offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
		newX = x + offset[0]
		newY = y + offset[1]
		if newX < 0 or newY < 0 or newX >= len(lines[0]) or newY >= len(lines[0]):
			continue
		match offset:
			case (0, 1):
				if lines[newY][newX] not in ['|', 'L', 'J']:
					continue
			case (1, 0):
				if lines[newY][newX] not in ['-', '7', 'J']:
					continue
			case (-1, 0):
				if lines[newY][newX] not in ['-', 'L', 'F']:
					continue
			case (0, -1):
				if lines[newY][newX] not in ['|', 'F', '7']:
					continue

		success, length = followPath(lines, x, y, newX, newY)
		if success:
			return length / 2
	return -1

if __name__ == '__main__':
	print("========== Part 1 ==========")
	print(f"Part 1 result: {part1()}")
	# print("========== Part 2 ==========")
	# print(f"Part 2 result: {part2()}")