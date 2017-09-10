#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Program "m" as the height
    // State that m can't be less than 0 or more than 23
    int m;
    do
    {
        m = get_int("height: ");
    }
    while (m < 0 || m > 23);
    // Define "i" as representing the line number
    // Define "s" as the amount of spaces each line has
    // Define "h" as the amount of hashes each line has
    for (int i = 0; i < m; i++)
    {
        for (int s = 0; s < m - 1 - i; s++)
        {
            printf(" ");
        }
        for (int h = 0; h < i + 2; h++)
        {
            printf("#");
        }
        printf("\n");
    }
}