#include <stdio.h>

// Recursive
int rfib(int n)
{
    if(n <= 1) return n;
    return rfib(n-2) + rfib(n-1);
}

// Iterative
int ifib(int n)
{
    int t0=0, t1=1, s=0; i;
    if(n <= 1) return n;
    for(i=2; i<=n; i++)
    {
        s = t0 + t1;
        t0 = t1;
        t1 = s;
    }
    
    return s;
}

// Memoization
int F[10];

int mfib(int n)
{
    int i;
    for(i=0; i<10; i++)
        F[i] = -1;
    
    if(n <= 1)
    {
        F[n] = n;
        return n;
    }
    
    if(F[n-2] == -1)
        F[n-2] = mfib(n-2);
    if(F[n-1] == -1)
        F[n-1] = mfib(n-1);
    
    F[n] = F[n-2] + F[n-1];
    return F[n];
}

int main()
{
    printf("%d \n", mfib(5));
    return 0;
}
