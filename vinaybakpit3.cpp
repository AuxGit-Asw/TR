#include <stdio.h>
#include <string.h>

bool isPrime(int n)
{
    if (n <= 1)  return false;
    if (n <= 3)  return true;
   
    if (n%2 == 0 || n%3 == 0) return false;
   
    for (int i=5; i*i<=n; i=i+6)
        if (n%i == 0 || n%(i+2) == 0)
           return false;
   
    return true;
}

int append_to_reach_nearest_prime(int input1[], int input2)
{
    int sum = 0;
    for (int i = 0; i < input2; i++)
        sum += input1[i];

    int curr = sum - 1;
    int temp;

    while (1)
    {
        curr++;
        if (isPrime(curr))
            return curr - sum;
    }
}

int main()
{
    int arr[] = {21, 22, 23, 17};
    printf("%d\n", append_to_reach_nearest_prime(arr, 4));
}