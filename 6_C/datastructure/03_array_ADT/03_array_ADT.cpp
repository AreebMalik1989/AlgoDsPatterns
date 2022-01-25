#include <iostream.h>

using namespace std;

class Array {
private:
    int *A;
    int size;
    int length;
    void swap(int *x, int *y);

public:
    Array()
    {
        size = 10;
        length = 0;
        A = new int[size];
    }
    
    Array(int sz)
    {
        size = sz;
        length = 0;
        A = new int[size];
    }
    
    ~Array()
    {
        delete []A;
    }
    
    void Display();
    void Append(int x);
    void Insert(int index, int x);
    int Delete(int index);
    int LinearSearch(int key);
    int BinarySearch(int key);
    int RBinarySearch(int key);
    int Get(int index);
    void Set(int index, int x);
    int Max();
    int Min();
    int Sum();
    float Avg();
    void Reverse();
    void Reverse2();
    int isSorted();
    void InsertS(int x);
    void Rearrange();
    Array* Merge(Array arr2);
    Array* Union(Array arr2);
    Array* Intersection(Array arr2);
    Array* Difference(Array arr2);
}

void Array::swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

void Array::Display()
{
    int i;
    cout << "\nElements are\n";
    for(i=0; i<length; i++)
        cout << A[i]; << " ";
}

void Array::Append(int x)
{
    if(length < size)
        A[length++] = x;
}

void Array::Insert(int index, int x)
{
    int i;
    if(index >= 0 && index <= length)
    {
        for(i=length; i>index; i--)
            A[i] = A[i-1]
        A[index] = x;
        length++;
    }
}

int Array::Delete(int index)
{
    int x=0;
    int i;
    
    if(index >= 0 && index < length)
    {
        x = A[index];
        for(i=index; i<length-1; i--)
            A[i] = A[i+1]
        length--;
        return x;
    }
    return 0;
}

int Array::LinearSearch(int key)
{
    int i;
    for(i=0; i<length; i++)
    {
        if(key == A[i])
        {
            swap(&A[i], A[0]);
            return i;
        }
    }
    return -1;
}

int Array::BinarySearch(int key)
{
    int l, mid, h;
    l = 0;
    h = length-1;
    while(l <= h)
    {
        mid = l + (h-l)/2;
        if(key < A[mid])
            h = mid-1;
        else if(key > A[mid])
            l = mid+1;
        else
            return mid;
    }
    return -1;
}

int Array::RBinarySearch(int key, int l, int h)
{
    int mid = 0;
    if(l <= h)
    {
        mid = (l+h)/2;
        if(key < A[mid])
            return RBinarySearch(key, l, mid-1);
        else if(key > A[mid])
            return RBinarySearch(key, mid+1, h);
        return mid;
    }
    return -1;
}

int Array::Get(int index)
{
    if(index >=0 && index < length)
        return A[index];
    return -1;
}

void Array::Set(int index, int x)
{
    if(index >=0 && index < length)
        A[index] = x;
}

int Array::Max()
{
    int max = A[0];
    int i;
    for(i=0; i<length; i++)
    {
        if(A[i] > max)
            max = A[i];
    }
    return max;
}

int Array::Min()
{
    int min = A[0];
    int i;
    for(i=0; i<length; i++)
    {
        if(A[i] < min)
            min = A[i];
    }
    return min;
}

int Array::Sum()
{
    int s = 0;
    int i;
    for(i=0; i<length; i++)
        s += A[i];
    return s;
}

float Array::Avg()
{
    return (float)Sum(arr)/length;
}

void Array::Reverse()
{
    int *B;
    int i, j;
    
    B = (int *)malloc(arr->length*sizeof(int));
    
    for(i=length-1, j=0; i>=0; i--, j++)
        B[j] = A[i];
    for(i=0; i<length; i++)
        A[i] = B[i];
}

void Array::Reverse2()
{
    int i, j;
    for(i=0, j=length-1; i<j; i++, j--)
        swap(&A[i], &A[j]);
}

int Array::isSorted()
{
    int i;
    for(i=0; i<length-1; i++)
    {
        if(A[i] > A[i+1])
            return 0;
    }
    return 1;
}

// Rearrange array such that all negatives are in left and positive in right
void Array::Rearrange()
{
    int i, j;
    i = 0;
    j = length-1;
    while(i<j)
    {
        while(A[i]<0) i++;
        while(A[j]>=0) j++;
        if(i<j) swap(&A[i], &A[j]);
    }
}

// Insert element in sorted array
void Array::InsertS(int x)
{
    int i = length-1;
    if(length == size)
        return;
    
    while(i >= 0 && A[i] > x)
    {
        A[i+1] = A[i];
        i--;
    }
    
    A[i+1] = x;
    length++;
}

// Merge sorted arrays
Array* Array::Merge(Array arr2)
{
    int i, j, k;
    i=j=k=0;
    
    Array *arr3 = new Array(length+arr2.length);
    
    while(i < length && j < arr2.length)
    {
        if(A[i] < arr2.A[j])
            arr3.A[k++] = A[i++];
        else
            arr3.A[k++] = arr2.A[j++];
    }
    
    while(i < length)
        arr3->A[k++] = A[i++];
    while(j < arr2->length)
        arr3->A[k++] = arr2.A[j++];
    
    arr3->length = length + arr2.length;
    
    return arr3;
}

// Union of sorted arrays
Array* Array::Union(Array arr2)
{
    int i, j, k;
    i=j=k=0;
    
    Array *arr3 = new Array(length + arr2.length);
    
    while(i < length && j < length)
    {
        if(A[i] < arr2.A[j])
            arr3->A[k++] = A[i++];
        else if(A[i] > arr2.A[j])
            arr3->A[k++] = arr2.A[j++];
        else
        {
            arr3->A[k++] = A[i++];
            j++;
        }
    }

    while(i < length)
        arr3->A[k++] = A[i++];
    while(j < arr2.length)
        arr3->A[k++] = arr2.A[j++];

    arr3->length = k;
    
    return arr3;
}

// Intersection of sorted arrays
Array* Array::Intersection(Array arr2)
{
    int i, j, k;
    i=j=k=0;
    
    struct Array *arr3 = new Array(length + arr2.length);
    
    while(i < length && j < arr2.length)
    {
        if(A[i] < arr2.A[j])
            i++;
        else if(A[i] > arr2.A[j])
            j++;
        else
        {
            arr3->A[k++] = A[i++];
            j++;
        }
    }
    
    arr3->length = k;
    
    return arr3;
}

// Difference of sorted arrays
Array* Array::Difference(Array arr2)
{
    int i, j, k;
    i=j=k=0;
    
    struct Array *arr3 = new Array(length + arr2.length);
    
    while(i < length && j < arr2.length)
    {
        if(A[i] < arr2.A[j])
            arr3->A[k++] = A[i++];
        else if(A[i] > arr2.A[j])
            j++;
        else
        {
            i++;
            j++;
        }
    }
    
    while(i < length)
        arr3->A[k++] = A[i];
    
    arr3->length = k;
    
    return arr3;
}
