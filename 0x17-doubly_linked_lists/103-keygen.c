#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * main - Keygen for crackme5.
 * @argc: Argument count.
 * @argv: Argument vector.
 *
 * Return: Always 0.
 */
int main(int argc, char *argv[])
{
	if (argc != 2)
	{
		fprintf(stderr, "Usage: %s <username>\n", argv[0]);
		return (EXIT_FAILURE);
	}
	char *username = argv[1];
	size_t len = strlen(username);
	unsigned char key = len ^ 59;

	for (size_t i = 0; i < len; i++)
		key += username[i];

	printf("%02x\n", key);
	return (EXIT_SUCCESS);
}
