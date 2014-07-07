#include<stdio.h>
#include<string.h>

// PROBLEM 1.3
// Remove the duplicate chars for a string
// (this version only considers the continuous duplicate chars)
void remove_continuous_duplicate_chars(char* str)
{
    int size = strlen(str);
    printf("Length of %s: %d\n", str, size);
    if (size <= 1)
        return;

    int cur_index = 0;
    int next_index = 1;

    while (next_index < size)
    {
        if(str[cur_index] != str[next_index])
        {
            ++cur_index;
            if (cur_index != next_index)
                str[cur_index] = str[next_index];
        }

        ++next_index;
    }

    ++cur_index;
    if (cur_index < size)
        str[cur_index] = '\0';
}


//main
int main()
{
    char str[] = "wwuhhaochheng";
    printf("Original: %s\n", str);
    remove_continuous_duplicate_chars(str);
    printf("Original: %s\n", str);
    return 0;
}
