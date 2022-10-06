#include <stdio.h>
#include <string.h>
#include <math.h>

#include <iostream>
using namespace std;

double quadratic_roots(int input1, int input2, int input3)
{
    double a = input1, b = input2, c = input3;
    double dis = b*b - 4*a*c;

    if (dis < 0)
        return 0;
    
    double r1 = (-b + sqrt(dis)) / (2*a);
    double r2 = (-b - sqrt(dis)) / (2*a);

    return (r1 + r2)/2;
}

int main()
{
    int a,b, c;
    cin>>a>>b>>c;
    cout<<quadratic_roots(a, b, c)<<endl;
}