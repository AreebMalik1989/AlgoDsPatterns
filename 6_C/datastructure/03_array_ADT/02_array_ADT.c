#include <stdio.h>
#include <stdlib.h>

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
        mid = l + (h-l)/2;
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

int Get(struct Array arr, int index)
{
    if(index >=0 && index < arr.length)
        return arr.A[index];
    return -1;
}

void Set(struct Array *arr, int index, int x)
{
    if(index >=0 && index < arr->length)
        arr->A[index] = x;
}

int Max(struct Array arr)
{
    int max = arr.A[0];
    int i;
    for(i=0; i<arr.length; i++)
    {
        if(arr.A[i] > max)
            max = arr.A[i];
    }
    return max;
}

int Min(struct Array arr)
{
    int min = arr.A[0];
    int i;
    for(i=0; i<arr.length; i++)
    {
        if(arr.A[i] < min)
            min = arr.A[i];
    }
    return min;
}

int Sum(struct Array arr)
{
    int s = 0;
    int i;
    for(i=0; i<arr.length; i++)
        s += arr.A[i];
    return s;
}

float Avg(struct Array arr)
{
    return (float)Sum(arr)/arr.length;
}

void Reverse(struct Array *arr)
{
    int *B;
    int i, j;
    
    B = (int *)malloc(arr->length*sizeof(int));
    
    for(i=arr->length-1, j=0; i>=0; i--, j++)
        B[j] = arr->A[i];
    for(i=0; i<arr->length; i++)
        arr->A[i] = B[i];
}

void Reverse2(struct Array *arr)
{
    int i, j;
    for(i=0, j=arr->length-1; i<j; i++, j--)
        swap(&arr->A[i], &arr->A[j]);
}

int isSorted(struct Array arr)
{
    int i;
    for(i=0; i<arr.length-1; i++)
    {
        if(arr.A[i] > arr.A[i+1])
            return 0;
    }
    return 1;
}

// Rearrange array such that all negatives are in left and positive in right
void Rearrange(struct Array *arr)
{
    int i, j;
    i = 0;
    j = arr->length-1;
    while(i<j)
    {
        while(arr->A[i]<0) i++;
        while(arr->A[j]>=0) j++;
        if(i<j) swap(&arr->A[i], &arr->A[j]);
    }
}

// Insert element in sorted array
void InsertS(struct Array *sortedArray, int x)
{
    int i = sortedArray->length-1;
    if(sortedArray->length == sortedArray->size)
        return;
    
    while(i >= 0 && sortedArray->A[i] > x)
    {
        sortedArray->A[i+1] = sortedArray->A[i];
        i--;
    }
    
    sortedArray->A[i+1] = x;
    sortedArray->length++;
}

// Merge sorted arrays
struct Array* Merge(struct Array *arr1, struct Array *arr2)
{
    int i, j, k;
    i=j=k=0;
    
    struct Array *arr3 = (struct Array *)malloc(sizeof(struct Array));
    
    while(i < arr1->length && j < arr2->length)
    {
        if(arr1->A[i] < arr2->A[j])
            arr3->A[k++] = arr1->A[i++];
        else
            arr3->A[k++] = arr2->A[j++];
    }
    
    while(i < arr1->length)
        arr3->A[k++] = arr1->A[i++];
    while(j < arr2->length)
        arr3->A[k++] = arr1->A[j++];
    
    arr3->length = arr1->length + arr2->length;
    arr3->size = 10;
    
    return arr3;
}

// Union of sorted arrays
struct Array* Union(struct Array *arr1, struct Array *arr2)
{
    int i, j, k;
    i=j=k=0;
    
    struct Array *arr3 = (struct Array *)malloc(sizeof(struct Array));
    
    while(i < arr->length && j < arr->length)
    {
        if(arr1->A[i] < arr2->A[j])
            arr3->A[k++] = arr1->A[i++];
        else if(arr1->A[i] > arr2->A[j])
            arr3->A[k++] = arr2->A[j++];
        else
        {
            arr3->A[k++] = arr1->A[i++];
            j++;
        }
    }

    while(i < arr1->length)
        arr3[k++] = arr1->A[i++];
    while(j < arr2->length)
        arr3[k++] = arr2->A[j++];

    arr3->length = k;
    arr3->size = 10;

    return arr3;
}

// Intersection of sorted arrays
struct Array* Intersection(struct Array *arr1, struct Array *arr2)
{
    int i, j, k;
    i=j=k=0;
    
    struct Array *arr3 = (struct Array*)malloc(sizeof(struct Array));
    
    while(i < arr1->length && j < arr2->length)
    {
        if(arr1->A[i] < arr2->A[j])
            i++;
        else if(arr1->A[i] > arr2->A[j])
            j++;
        else
        {
            arr3->A[k++] = arr1->A[i++];
            j++;
        }
    }
    
    arr3->length = k;
    arr3->size = 10;
    
    return arr3;
}

// Difference of sorted arrays
struct Array* Difference(struct Array *arr1, struct Array *arr2)
{
    int i, j, k;
    i=j=k=0;
    
    struct Array *arr3 = (struct Array*) malloc(sizeof(struct Array));
    
    while(i < arr1->length && j < arr2->length)
    {
        if(arr1->A[i] < arr2->A[j])
            arr3->A[k++] = arr1->A[i++];
        else if(arr1->A[i] > arr2->A[j])
            j++;
        else
        {
            i++;
            j++;
        }
    }
    
    while(i < arr->length)
        arr3->A[k++] = arr1->A[i];
    
    arr3->length = k;
    arr3->size = 10;
    
    return arr3;
}
