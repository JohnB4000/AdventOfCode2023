#include <stdio.h>
#include <string.h>


int part1(void);
int charArrayToInt(char charArray[], int length);
int part2(void);
int isNumber(char num);
int getStartIndex(char *line, int index);
int alreadyVisited(int list[6][2], int length, int x, int y);
int getNumber(char *line, int startIndex);


const char FILENAME[] = "input.txt";
const int OFFSETS[9][2] = {
				{-1, -1},
				{-1, 0},
				{-1, 1},
				{0, -1},
				{0, 1},
				{1, -1},
				{1, 0},
				{1, 1},
			};
int LINE_COUNT = 140;
int LINE_LENGTH = 141;
// int LINE_COUNT = 10;
// int LINE_LENGTH = 10;


int main(int argc, char const *argv[]) {
	printf("=========== Part 1 ============\n");
	int part1result = part1();
	if (part1result == -1) {
		printf("Part 1 failed");
		return 1;
	}
	printf("The sum of the part numbers is: %d\n", part1result);

	printf("=========== Part 2 ============\n");
	int part2result = part2();
	if (part2result == -1) {
		printf("Part 2 failed");
		return 1;
	}
	printf("The sum of the part numbers is: %d\n", part2result);
	return 0;
}


int part1() {
	int total = 0;
	char contents[LINE_COUNT][LINE_LENGTH+2];

	FILE *file = fopen(FILENAME, "r");
	if (file == NULL) {
		printf("Cannot read file: %s", FILENAME);
		return -1;
	}

	int i = 0;
	while (fgets(contents[i], sizeof(contents[i]), file) != NULL) {
		int length = strlen(contents[i]);
        if (length > 0 && contents[i][length - 1] == '\n') {
            contents[i][length - 1] = '\0';
        }
		i++;
	}

	int index = 0;

	int indices[3];
	char numbers[3];
	int indicesIndex = 0;

	for (int i = 0; i < LINE_COUNT; i++) {
		index = 0;
		while (contents[i][index] != '\0') {
			while (contents[i][index] > '9' || contents[i][index] < '0') {
				index++;
				if (index >= LINE_LENGTH) break;
			} 
			if (index >= LINE_LENGTH) break;

			indicesIndex = 0;
			while (contents[i][index] >= '0' && contents[i][index] <= '9') {
				numbers[indicesIndex] = contents[i][index];
				indices[indicesIndex++] = index;
				index++;
			}

			int offsetI;
			int offsetIndex;

			int notAddedYet = 1;

			for (int x = 0; x < indicesIndex; x++) {			
				for (int offset = 0; offset < 8; offset++) {
					offsetI = i + OFFSETS[offset][0];
					offsetIndex = indices[x] + OFFSETS[offset][1];
					if (offsetI >= 0 && offsetI < LINE_COUNT && offsetIndex >= 0 && offsetIndex <= LINE_LENGTH) {
						char charToCheck = contents[offsetI][offsetIndex];
						if ((charToCheck > '9' || charToCheck < '0') && charToCheck != '.' && charToCheck != '\0') {
							if (notAddedYet) {
								total += charArrayToInt(numbers, indicesIndex);
								notAddedYet = 0;
							}
						}
					}
				}
			}
		}
	}

	fclose(file);
	return total;
}


int charArrayToInt(char charArray[], int length) {
    int result = 0;

    for (int i = 0; i < 3 && charArray[i] >= '0' && charArray[i] <= '9' && i < length; ++i) {
        result = result * 10 + (charArray[i] - '0');
    }

    return result;
}


int part2() {
	int total = 0;
	char contents[LINE_COUNT][LINE_LENGTH+2];

	FILE *file = fopen(FILENAME, "r");
	if (file == NULL) {
		printf("Cannot read file: %s", FILENAME);
		return -1;
	}

	int i = 0;
	while (fgets(contents[i], sizeof(contents[i]), file) != NULL) {
		int length = strlen(contents[i]);
        if (length > 0 && contents[i][length - 1] == '\n') {
            contents[i][length - 1] = '\0';
        }
		i++;
	}

	int index = 0;

	int indices[3];
	char numbers[3];
	int indicesIndex = 0;

	for (int i = 0; i < LINE_COUNT; i++) {
		index = 0;
		while (contents[i][index] != '\0') {
			while (contents[i][index] != '*') {
				index++;
				if (index >= LINE_LENGTH) break;
			} 
			if (index >= LINE_LENGTH) break;
			// printf("%d\n", index);


			int startIndices[6][2];
			int startIndicesIndex = 0;
			int startIndex;

			int offsetI;
			int offsetIndex;

			for (int offset = 0; offset < 8; offset++) {
				offsetI = i + OFFSETS[offset][0];
				offsetIndex = index + OFFSETS[offset][1];
				if (offsetI >= 0 && offsetI < LINE_COUNT && offsetIndex >= 0 && offsetIndex <= LINE_LENGTH) {
					char charToCheck = contents[offsetI][offsetIndex];
					if (isNumber(charToCheck)) {
						startIndex = getStartIndex(contents[offsetI], offsetIndex);
						if (alreadyVisited(startIndices, startIndicesIndex, offsetI, startIndex) == 0) {
							startIndices[startIndicesIndex][0] = offsetI;
							startIndices[startIndicesIndex++][1] = startIndex;
						}
					}
				}
			}

			if (startIndicesIndex == 2) {
				printf("%d\n", getNumber(contents[startIndices[0][0]], startIndices[0][1]));
				total += getNumber(contents[startIndices[0][0]], startIndices[0][1]) * getNumber(contents[startIndices[1][0]], startIndices[1][1]);
			}


			// indicesIndex = 0;
			// while (contents[i][index] >= '0' && contents[i][index] <= '9') {
			// 	numbers[indicesIndex] = contents[i][index];
			// 	indices[indicesIndex++] = index;
			// 	index++;
			// }

			index++;
		}
	}

	fclose(file);
	return total;
}


int isNumber(char num) {
	return num >= '0' && num <= '9';
}


int getStartIndex(char *line, int index) {
	while (index >= 0 && isNumber(line[index])) {
		index--;
	}
	return index+1;
}


int alreadyVisited(int list[6][2], int length, int x, int y) {
	for (int i = 0; i < length; i++) {
		if (list[i][0] == x && list[i][1] == y) {
			return 1;
		}
	}
	return 0;
}


int getNumber(char *line, int startIndex) {
	char nums[3];
	int numsIndex = 0;
	while (isNumber(line[startIndex])) {
		nums[numsIndex++] = line[startIndex++]; 
	}
	return charArrayToInt(nums, numsIndex);
}