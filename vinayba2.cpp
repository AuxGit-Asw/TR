#include <stdio.h>
#include <string.h>

int count_of_words(char* input1)
{
    int count = 0;
    for (int i = 0; i < strlen(input1); i++)
    {
        if (input1[i] == ' ')
            count++;
    }
    return count + 1;
}