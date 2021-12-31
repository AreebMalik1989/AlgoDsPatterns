#include <stdio.h>

int power(int m, int n)
{
    if(n == 0)
        return 1;
    return power(m, n-1) * m;
}

int power_efficient(int m, int n)
{
    if(n == 0)
        return 1;
    if(n % 2 == 0)
        return power_efficient(m*m, n/2);
    return m * power_efficient(m*m, (n-1)/2);
}

int main()
{
    int r = power_efficient(9, 3);
    printf("%d ", r);
    return 0;
}
