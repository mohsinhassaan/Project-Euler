#include <stdio.h>

unsigned long long g[21][21];

int main()
{
    for (int i = 0; i < 21; ++i)
    {
        g[i][0] = 1;
        g[0][i] = 1;
    }

    for (int i = 0; i < 21; i++)
    {
        for (int j = 0; j < 21; j++)
        {
            printf("%lld ", g[i][j]);
        }
        printf("\n");
    }

    for (int i = 1; i < 21; ++i)
    {
        for (int j = 1; j < 21; ++j)
        {
            g[i][j] = g[i - 1][j] + g[i][j - 1];
        }
    }

    FILE *file = fopen("lat.txt", "w");

    for (int i = 0; i < 21; i++)
    {
        for (int j = 0; j < 21; j++)
        {
            fprintf(file, "%lld ", g[i][j]);
        }
        fprintf(file, "\n");
    }

    printf("%lld\n", g[20][20]);
    return 0;
}