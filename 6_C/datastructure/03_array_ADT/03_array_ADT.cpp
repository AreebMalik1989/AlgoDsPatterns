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

