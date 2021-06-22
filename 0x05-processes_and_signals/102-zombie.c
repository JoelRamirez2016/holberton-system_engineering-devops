#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - This function create a infinity loop
 * Return: Always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - This program create 5 process executing a infinity loop
 * Return: Always 0
 */
int main(void)
{
	int i;
	pid_t pid_current;

	for (i = 0; i < 5; i++)
	{
		pid_current = fork();

		if (pid_current > 0)
			printf("Zombie process created, PID: %i\n", pid_current);
		else
			return (0);
	}

	infinite_while();
	return (0);
}
