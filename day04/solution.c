#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int part1(void);
int checkCardForPoints(char *line);
int isNumber(char num);
int getNumberOfWinningNumbers(char *line);
int charArrayToInt(char charArray[], int length);
int part2(void);
int checkCardForCards(int lineCount, char (*contents)[300], int index);


char FILENAME[] = "input.txt";


int main(int argc, char const *argv[]) {
	printf("=========== Part 1 ============\n");
	int part1result = part1();
	if (part1result == -1) {
		printf("Part 1 failed");
		return 1;
	}
	printf("There are %d points.\n", part1result);

	printf("=========== Part 2 ============\n");
	int part2result = part2();
	if (part2result == -1) {
		printf("Part 2 failed");
		return 1;
	}
	printf("There are %d cards\n", part2result);

	return 0;
}


int part1() {
	int total = 0;
	char line[300];

	FILE *file = fopen(FILENAME, "r");
	if (file == NULL) {
		printf("Cannot read file: %s", FILENAME);
		return -1;
	}

	while (fgets(line, sizeof(line), file) != NULL) {
		int length = strlen(line);
        if (length > 0 && line[length - 1] == '\n') {
            line[length - 1] = '\0';
        }
		total += checkCardForPoints(line);
	}

	fclose(file);
	return total;
}


int checkCardForPoints(char *line) {
	int total = 0;

	int numWinningNums = getNumberOfWinningNumbers(line);
	int *winningNums = (int*) malloc(numWinningNums * sizeof(int));
	int winningNumsIndex = 0;
	if (winningNums == NULL) {
        printf("Memory allocation failed\n");
        return -1;
    }

	int index = 0;
	char nums[2];
	int numsIndex = 0;

	while (line[index] != ':') index++;
	while (isNumber(line[index]) == 0) index++;

	while (line[index] != '|') {
		if (line[index] == ' ') index++;
		numsIndex = 0;
		while (isNumber(line[index])) {
			nums[numsIndex++] = line[index++];
		}
		index++;
		winningNums[winningNumsIndex++] = charArrayToInt(nums, numsIndex);
	}
	
	while (isNumber(line[index]) == 0) index++;
	int currentNumber;

	while (line[index] != '\0') {
		numsIndex = 0;
		while (isNumber(line[index])) {
			nums[numsIndex++] = line[index++];
		}
		index++; 
		currentNumber = charArrayToInt(nums, numsIndex);
		for (int i = 0; i < numWinningNums; i++) {
			if (currentNumber == winningNums[i]) {
				total = (total == 0) ? 1 : total * 2;
				break;
			}
		}
	}

	free(winningNums);
	return total;
}


int isNumber(char num) {
	return num >= '0' && num <= '9';
}


int getNumberOfWinningNumbers(char *line) {
	int winningCount = 0;
	int index = 0;
	while (line[index] != ':') index++;
	while (isNumber(line[index]) == 0) index++;
	while (line[index] != '|') {
		if (line[index] == ' ') index++;
		winningCount++;
		while (isNumber(line[index])) index++;
		index++;
	}
	return winningCount;
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
	char line[300];

	FILE *file = fopen(FILENAME, "r");
	if (file == NULL) {
		printf("Cannot read file: %s", FILENAME);
		return -1;
	}

	int lineCount = 0;
	while (fgets(line, sizeof(line), file) != NULL) {
		lineCount++;
	}

    fseek(file, 0, SEEK_SET);

	char (*contents)[300] = malloc(lineCount * sizeof(char[300]));
	if (contents == NULL) {
        printf("Memory allocation failed\n");
        return -1;
    }

	int i = 0;
	while (i < lineCount && fgets(contents[i], sizeof(char[300]), file) != NULL) {
		i++;
	}

	for (int i = 0; i < lineCount; i++) {
		total += checkCardForCards(lineCount, contents, i);
	}

	// printf("Contents of the 2D array:\n");
    // for (int j = 0; j < i; ++j) {
    //     printf("%s", contents[j]);
    // }
	// printf("\n");

	free(contents);

	fclose(file);
	return total + lineCount;
}


int checkCardForCards(int lineCount, char (*contents)[300], int lineIndex) {
	char *line = contents[lineIndex];
	int totalWins = 0;

	int numWinningNums = getNumberOfWinningNumbers(line);
	int *winningNums = (int*) malloc(numWinningNums * sizeof(int));
	int winningNumsIndex = 0;
	if (winningNums == NULL) {
        printf("Memory allocation failed\n");
        return -1;
    }

	int index = 0;
	char nums[2];
	int numsIndex = 0;

	while (line[index] != ':') index++;
	while (isNumber(line[index]) == 0) index++;

	while (line[index] != '|') {
		if (line[index] == ' ') index++;
		numsIndex = 0;
		while (isNumber(line[index])) {
			nums[numsIndex++] = line[index++];
		}
		index++;
		winningNums[winningNumsIndex++] = charArrayToInt(nums, numsIndex);
	}
	
	while (isNumber(line[index]) == 0) index++;
	int currentNumber;

	while (line[index] != '\0') {
		numsIndex = 0;
		while (isNumber(line[index])) {
			nums[numsIndex++] = line[index++];
		}
		index++; 
		currentNumber = charArrayToInt(nums, numsIndex);
		for (int i = 0; i < numWinningNums; i++) {
			if (currentNumber == winningNums[i]) {
				totalWins++;
				break;
			}
		}
	}

	// printf("Card %d wins %d\n", lineIndex+1, totalWins);
	free(winningNums);
	int futureWins = 0;
	for (int i = 0; i < totalWins; i++) {
		if (lineIndex + i + 1 <= lineCount) {
			futureWins += checkCardForCards(lineCount, contents, lineIndex + i + 1);
		}
	}
	return totalWins + futureWins;
}