#include <stdio.h>

int fact(int n)
{
    if(n==0) return 1;
    return fact(n-1) * n;
}

// Iterative
int I_nCr(int n, int r)
{
    int numerator, denominator;
    numerator = fact(n);
    denominator = fact(r) * fact(n-r);
    return nemerator / denominator;
}

// Recursive
int nCr(int n, int r)
{
    if(n==r || r==0)
        return 1;
    return nCr(n-1, r-1) + nCr(n-1, r);
}

int main()
{
    printf("%d \n", nCr(5, 3));
    return 0;
}
