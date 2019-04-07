#include <stdio.h>

int d(int n);

int main(int argc, char const *argv[])
{
    int total = 0;
    for (int a = 0; a < 10000; a++)
    {
        for (int b = 0; b < a; b++)
        {
            if (d(a) == b && d(b) == a)
            {
                total += a + b;
                printf("%d, %d\n", a, b);
            }
        }
    }
    printf("%d\n", total);
    return 0;
}

int d(int n)
{
    int total = 0;
    for (int i = 1; i <= n / 2; i++)
    {
        if (n % i == 0)
        {
            total += i;
        }
    }
    return total;
}
