#include <stdio.h>

int main(int argc, char const *argv[])
{
    int size = 2000000;
    int lst[size];
    double sum = 0;
    for (int i = 0; i < size; i++)
    {
        lst[i] = i;
    }

    lst[0] = lst[1] = 0;

    for (int i = 0; i < size; i++)
    {
        if (lst[i] != 0)
        {
            // printf("%d, %d\n", i, lst[i]);
            for (int j = i * 2; j < size; j += i)
            {
                // printf("%d\n", lst[j]);
                lst[j] = 0;
            }
            sum += lst[i];
        }
    }

    printf("%0.0f\n", sum);

    return 0;
}
