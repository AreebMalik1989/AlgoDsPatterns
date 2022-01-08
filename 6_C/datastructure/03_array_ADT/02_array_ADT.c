#include <stdio.h>

struct Array
{
    int A[10];
    int size;
    int length;
}

void swap(int *x, int *y)
{
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

void Display(struct Array arr)
{
    int i;
    printf("\nElements are:\n");
    for(i=0; i<arr.length; i++)
        printf("%d " arr.A[i]);
}

void Append(struct Array *arr, int x)
{
    if(arr->length < arr->size)
        arr->A[arr->length++] = x;
}

void Insert(struct Array *arr, int x, int index)
{
    int i;
    if(index>=0 && index <= arr->length)
    {
        for(i=arr->length; i>index; i--)
            arr->A[i] = arr->A[i-1];
        arr->A[index] = x;
        arr->length++;
    }
}

void Delete(struct Array *arr, int index)
{
    int x=0;
    int i;
    if(index>=0 && index < arr->length)
    {
        x = arr->A[index];
        for(i=index; i < arr->length-1; i++)
            arr->A[i] = arr->A[i+1];
        arr->length--;
        return x;
    }
    return 0;
}

int LinearSearch(struct Array *arr, int key)
{
    int i;
    for(i=0; i<arr->length; i++)
    {
        if(key == arr.A[i])
        {
            // swapping improves linear search performance
            // for frequently searched elements by bringing
            // them in beginning of array
            swap(&arr.A[i], &arr.A[i-1]);
            return i;
        }
    }
    return -1;
}

int BinarySearch(struct Array arr, int key)
{
    int l, mid, h;
    l = 0;
    h = arr.length-1;
    while(l <= h)
    {
        mid = (l+h)/2;
        if(key < arr.A[mid])
            h = mid-1;
        else if(key > arr.A[mid])
            l = mid+1;
        else
            return mid;
    }
    return -1;
}

int RBinarySearch(struct Array arr, int key, int l, int h)
{
    int mid = 0;
    if(l <= h)
    {
        mid = (l+h)/2;
        if(key < arr.A[mid])
            return RBinarySearch(arr, key, l, mid-1);
        else if(key > arr.A[mid])
            return RBinarySearch(arr, key, mid+1, h);
        return mid;
    }
    return -1;
}
