#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - this fucntion checks whether a given linked
 * list is a palindrome or not.
 *
 * @head: the list that is being checked
 *
 * Description: refer to the first commented out line
 *
 * Return: returns 1 if the list is a palindrome, returns 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *current;
	int i, j, length;
	char *chupapi;

	if (*head == NULL)
	{
		return (1);
	}
	current = *head;
	length = 0;
	while (current != NULL)
	{
		length++;
		current = current->next;
	}

	chupapi = malloc(length * sizeof(char));
	current = *head;
	i = 0;

	while (current != NULL)
	{
		chupapi[i] = current->n;
		i++;
		current = current->next;
	}

	j = 0;

	while (j <= (i - 1) / 2)
	{
		if (chupapi[j] != chupapi[i - 1 - j])
		{
			free(chupapi);
			return (0);
		}
		j++;
	}
	free(chupapi);
	return (1);
}

