#include <stdio.h>
#include <string.h>

int sum_of_factors_triangular_number(int input1)
{
    long int tri = (input1*(input1 + 1))/2;
    int sum = 0;
    for (int i = 1; i < tri; i++)
    {
        if (tri % i == 0)
            sum += i;
    }
    return sum;
}

int main()
{
    int x, y;
    while(1)
    {
        scanf("%d", &x);
        printf("%d\n", sum_of_factors_triangular_number(x));
    }
}
