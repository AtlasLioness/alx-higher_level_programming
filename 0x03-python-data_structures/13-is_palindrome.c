#include "lists.h"
/**
 * reversed_list - reverses a singly linked list
 * @head: starting node of the singly linked list to reverse
 *
 * Return: pointer to the new reversed singly linked list
 */
listint_t *reversed_list(listint_t **head)
{
	listint_t *previous = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}
	return (previous);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head node of the singly linked list
 *
 * Return: 0 if it is not a palindrome or 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *reversed;

	if (head == NULL)
		return (1);
	reversed = reversed_list(head);

	while (reversed && current)
	{
		if (reversed->n == current->n)
		{
			reversed = reversed->next;
			current = current->next;
		}
		else
			return (0);
	}
	if (!current)
		return (1);

	return(0);
}
