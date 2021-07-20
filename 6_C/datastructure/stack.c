#include <stdio.h>
#include <stdlib.h>

struct node
{
	int data;
	struct node *next;
	struct node *prev;
} *head, *tmp;

int count = 0;

void create();
void push(int x);
int pop();
int peek();
int size();
int isEmpty();

void create()
{
	head = NULL;
}

void push(int x)
{
	if(head == NULL)
	{
		head = (struct node *) malloc(1 * sizeof(struct node));
		head->next = NULL;
		head->prev = NULL;
		head->data = x;
	}
	else
	{
		tmp = (struct node *) malloc(1 * sizeof(struct node));
		tmp->data = x;
		tmp->next = NULL;
		tmp->prev = head;
		head->next = tmp;
		head = tmp;
	}
	count++;
}

int pop() {
	int returnData;
	if(head == NULL)
	{
		printf("Error: Empty stack");
		exit(1);
	}
	else
	{
		returnData = head->data;
		if(head->prev == NULL)
		{
			free(head);
			head = NULL;
		}
		else
		{
			head = head->prev;
			free(head->next);
		}
	}
	count--;
	return returnData;
}

int peek()
{
	if(head != NULL)
	{
		return head->data;
	}
	else
	{
		printf("Error: Peeking from empty stack.");
		exit(1);
	}
}

int size() {
	return count;
}

int isEmpty()
{
	if(count == 0)
	{
		return 1;
	}
	return 0;
}

int main()
{
	int x, y, z;

	create();
	push(4);
	x = pop();
	printf("%d.\t\tCount: %d.\tEmpty: %d.\n", x, size(), isEmpty());

	push(1);
	push(2);
	push(3);
	x = pop();
	y = pop();
	printf("%d, %d.\t\tCount: %d.\tEmpty: %d.\n", x, y, size(), isEmpty());

	pop();
	push(5);
	push(6);
	x = peek();
	push(7);
	y = pop();
	push(8);
	z = pop();

	printf("%d, %d, %d.\tCount: %d.\tEmpty: %d.\n", x, y, z, size(), isEmpty());
	return 0;
}
