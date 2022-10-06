#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;

int gcd(int input1, int input2)
{
  if (input2 == 0)
    return input1;
  return gcd(input2, input1 % input2);
}
 
int lcm(int input1, int input2)
{
    return (input1 / gcd(input1, input2)) * input2;
}


int lcm_gcd_diff(int input1, int input2)
{
    return lcm(input1, input2) - gcd(input1, input2);
}

int main()
{
    int a, b;
    a = 28;
    b = 35;

    cout<<lcm_gcd_diff(a, b)<<endl;
}