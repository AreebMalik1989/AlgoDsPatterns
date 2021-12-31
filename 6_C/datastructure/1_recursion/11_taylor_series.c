#include <stdio.h>

double e(int x, int n)
{
    static double p=1, f=1;
    double r;
    
    if(n == 0)
        return 1;
    r = e(x, n-1);
    p = p * x;
    f = f * n;
    return r + (p/f);
}

// Taylor's Series Honer's Rule
double eh(int x, int n)
{
    static double s;
    if(n == 0)
        return s;
    s = 1 + (x*s/n);
    return eh(x, n-1);
}

int main()
{
    printf("%lf \n", e(4, 15));
    return 0;
