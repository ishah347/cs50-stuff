#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    float change;
    // Set the initial amount of coins to 0
    int coins = 0;
    // Program so that the inserted change amount is not negative
    do
    {
        change = get_float("Change owed: ");
    }
    while (change < 0);
    // Multiply dollar amount by 100
    change = change * 100;
    // Round change to prevent errors
    int r = round(change);
    // Go down the list of quarters, dimes, nickels, and pennies, and ensure that the code tries to convert the change to coins in that order of preference
    // Ensure that the amount of coins increases by 1 whenever the change is converted
    while (r >= 25)
    {
        r = r - 25;
        coins = coins + 1;
    }
    while (r >= 10)
    {
        r = r - 10;
        coins = coins + 1;
    }
    while (r >= 5)
    {
        r = r - 5;
        coins = coins + 1;
    }
    while (r >= 1)
    {
        r = r - 1;
        coins = coins + 1;
    }
    // Have code display amount of coins
    printf("%i\n", coins);
}