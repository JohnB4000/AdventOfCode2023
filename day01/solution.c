#include <stdio.h>
#include <string.h>


int part1(void);
int part2(void);
int checkLine(char *nextLine);
int compare(const char *fixedLenStr, char *str2);
int checkForNumber(char *chars);


const char FILENAME[] = "input.txt";
const char NUMBERS[][6] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};


int main(int argc, char const *argv[]) {
	printf("=========== Part 1 ============\n");
	int part1result = part1();
	if (part1result == -1) {
		printf("Part 1 failed");
		return 1;
	}
	printf("The calibration number is: %d\n", part1result);

	printf("=========== Part 2 ============\n");
	int part2result = part2();
	if (part2result == -1) {
		printf("Part 2 failed");
		return 1;
	}
	printf("The calibration number is: %d\n", part2result);

	return 0;
}


int part1() {
	int total = 0;
	char nextLine[100];
	int nums[100];
	int numsIndex = 0;

	FILE *file = fopen(FILENAME, "r");
	if (file == NULL) {
		printf("Cannot read file: %s", FILENAME);
		return -1;
	}

	while(fscanf(file, "%99s", &nextLine) == 1) {
		numsIndex = 0;
		for (int i = 0; i < 99; i++) {
			if (nextLine[i] == '\0') break;

			if (nextLine[i] >= '0' && nextLine[i] <= '9') {
				nums[numsIndex++] = nextLine[i] - '0';
			}
		}

		total += (nums[0] * 10) + nums[numsIndex-1];
	}

	fclose(file);
	return total;
}


int part2() {
	int total = 0;
	char nextLine[100];

	FILE *file = fopen(FILENAME, "r");
	if (file == NULL) {
		printf("Cannot read file: %s", FILENAME);
		return -1;
	}

	int i = 1;
	while (fscanf(file, "%99s", &nextLine) == 1)
		total +=  checkLine(nextLine);

	fclose(file);
	return total;
}


int checkLine(char *line) {
	int nums[100];
	int numsIndex = 0;

	int i = 5;
	int result;

	char chars[5];

	for (int i = 0; i < 5; i++) {
		chars[i] = line[i];
	}

	while (1) {
		result = checkForNumber(chars);
		if (result != -1)
			nums[numsIndex++] = result;

		if (line[i] == '\0' || strlen(chars) < 5) {
			for (int j = 0; j < 5; j++) {
				for (int k = 0; k < 5; k++)	{
					if (k < strlen(chars))
						chars[k] = chars[k+1];
				}		
				result = checkForNumber(chars);
				if (result != -1) {
					nums[numsIndex++] = result;
				}
			}
			break;
		}

		for (int j = 0; j < 5; j++)
			chars[j] = chars[j+1];

		chars[4] = line[i++];
	}

	return (nums[0] * 10) + nums[numsIndex-1];
}


int compare(const char *fixedLenStr, char *str2) {
	int match = 0;
	for (int k = 0; k < strlen(fixedLenStr); k++) {
		if (str2[k] != fixedLenStr[k]) {
			match = 0;
			break;
		}
		match = 1;
	}
	return match;
}


int checkForNumber(char *chars) {
	int number = -1;

	if (chars[0] >= '0' && chars[0] <= '9')
		number = chars[0] - '0';

	for (int k = 0; k < 9; k++)
		if (compare(NUMBERS[k], chars) == 1)
			number = k+1;

	return number;
}