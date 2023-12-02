#include <stdio.h>
#include <string.h>


int part1(void);
int isValidGame(char *line);
int gamePower(char *line);
int part2(void);
int gamePower(char *line);


char FILENAME[] = "input.txt";
int MAX_RED = 12;
int MAX_GREEN = 13;
int MAX_BLUE = 14;


int main(int argc, char const *argv[]) {
	printf("=========== Part 1 ============\n");
	int part1result = part1();
	if (part1result == -1) {
		printf("Part 1 failed");
		return 1;
	}
	printf("The total of valid games is: %d\n", part1result);

	printf("=========== Part 2 ============\n");
	int part2result = part2();
	if (part2result == -1) {
		printf("Part 2 failed");
		return 1;
	}
	printf("The total power is: %d\n", part2result);

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

	int i = 1;
	while (fgets(line, sizeof(line), file) != NULL) {
		size_t length = strlen(line);
        if (length > 0 && line[length - 1] == '\n') {
            line[length - 1] = '\0';
        }
		if (isValidGame(line)) {
			total += i;
		}
		i++;
	}

	fclose(file);
	return total;
}


int isValidGame(char *line) {
	char nums[2];
	int numIndex = 0;

	int index = 6;
	while (line[index] != ':')
		index++;
	index++;
	
	while (line[index]  != '\0') {
		numIndex = 0;

		while (line[index] < '0' || line[index] > '9') {
			if (index >= strlen(line)) return 1; 
			index++;
		}

		while (line[index] != ' ') {
			nums[numIndex++] = line[index++];
		}

		int number = (numIndex == 2) ? (nums[0]-'0') * 10 + (nums[1]-'0') : (nums[0]-'0');

		switch (line[++index])	{
		case 'r':
			if (number > MAX_RED) return 0;
			break;
		case 'g':
			if (number > MAX_GREEN) return 0;
			break;
		case 'b':
			if (number > MAX_BLUE) return 0;
			break;
		}
	}

	return 1;
}


int part2() {
	int total = 0;
	char line[300];

	FILE *file = fopen(FILENAME, "r");
	if (file == NULL) {
		printf("Cannot read file: %s", FILENAME);
		return -1;
	}

	while (fgets(line, sizeof(line), file) != NULL) {
		size_t length = strlen(line);
        if (length > 0 && line[length - 1] == '\n') {
            line[length - 1] = '\0';
        }
		total += gamePower(line);
	}

	fclose(file);
	return total;
}


int gamePower(char *line) {
	int highestRed = -1;
	int highestGreen = -1;
	int highestBlue = -1;

	char nums[2];
	int numIndex = 0;

	int index = 6;
	while (line[index] != ':')
		index++;
	index++;
	
	while (line[index != '\0']) {
		numIndex = 0;

		while (line[index] < '0' || line[index] > '9') {
			if (index >= strlen(line)) return highestRed * highestGreen * highestBlue; 
			index++;
		}

		while (line[index] != ' ') {
			nums[numIndex++] = line[index++];
		}

		int number = (numIndex == 2) ? (nums[0]-'0') * 10 + (nums[1]-'0') : (nums[0]-'0');
		
		switch (line[++index])	{
		case 'r':
			if (number > highestRed) highestRed = number;
			break;
		case 'g':
			if (number > highestGreen) highestGreen = number;
			break;
		case 'b':
			if (number > highestBlue) highestBlue = number;
			break;
		}
	}

	return highestRed * highestGreen * highestBlue;
}