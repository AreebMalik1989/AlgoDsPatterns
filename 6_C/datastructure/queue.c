#include <stdio.h>
#include <stdlib.h>

struct node
{
	int data;
	struct node *next;
	struct node *prev;
} *head, *tail, *tmp;

int count;

void create();
void enqueue(int x);
int dequeue();
int peek();
int size();
int isEmpty();

void create()
{
	head = NULL;
	tail = NULL;
}

void enqueue(int x)
{
	if(head == NULL)
	{
		head = (struct node *) malloc(sizeof(struct node));
		head->data = x;
		head->prev = NULL;
		tail = head; 
	}
	else
	{
		tmp = (struct node *) malloc(sizeof(struct node));
		tmp->data = x;
		tmp->prev = NULL;
		tail = tmp;
	}
}

int dequeue()
{
	int returnData;
	if(head == NULL)
	{
		printf("Error: Dequeue from empty Queue.\n");
		exit(1);
	}
	else
	{
		returnData = head->data;
		if(head->prev == NULL)
		{
			head = NULL;
		}
		else
		{
			head = head->prev;
		}
		head->next = NULL;
	}
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
		printf("Error: Peeking from empty queue.\n");
		exit(1);
	}
}

int size()
{
	return count;
}

int isEmpty() {
	if(count == 0)
	{
		return 1;
	}
	return 0;
}
