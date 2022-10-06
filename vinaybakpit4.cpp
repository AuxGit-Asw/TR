#include <stdio.h>
#include <string.h>
#include <iostream>

using namespace std;

int validate_date_string(char* input1)
{
    int mv[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    int d = (input1[0] - '0')*10 + (input1[1] - '0');
    int m = (input1[3] - '0')*10 + (input1[4] - '0');
    int y = (input1[6] - '0')*1000 + (input1[7] - '0')*100 + (input1[8] - '0')*10 + (input1[9] - '0');

    if (((y % 4 == 0) && (y % 100 != 0)) || (y % 400 == 0))
        mv[1]++;

    if (m <= 0 || m > 12)
        return m;
    if (d <= 0 || d > mv[m - 1])
        return d;
    return 0;
}

int main()
{

        printf("%d\n", validate_date_string("29/02/2015"));

}