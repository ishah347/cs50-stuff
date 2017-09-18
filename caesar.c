#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    // Differentiate between a valid entry and an invalid entry
    if (argc == 2)
    {
        // Use argv[1] value as key integer
        int k = atoi(argv[1]);
        // Set up "plaintext" prompt
        string pl;
        {
            pl = get_string("plaintext: ");
        }
        // Set up "ciphertext" segment
        printf("ciphertext: ");
        for (int i = 0, n = strlen(pl); i < n; i++)
        {
            char f = pl[i];
            // Ensure plaintext entry is alphabetical
            if (isalpha(f))
            {
                // Differentiate between uppercase and lowercase entries in order to preserve case
                if (isupper(f))
                {
                    // Use key to instigate code
                    // Go from ASCII to alphabetical index to ASCII
                    char C = (f - 65 + k) % 26 + 65;
                    // Print the ciphertext
                    printf("%c", C);
                }
                if (islower(f))
                {

                    // Use key to instigate code
                    // Go from ASCII to alphabetical index to ASCII
                    char c = (f - 97 + k) % 26 + 97;
                    // Print the ciphertext
                    printf("%c", c);
                }
            }
        }
        printf("\n");
        return 0;
    }
    else
    {
        printf("Usage: ./caesar k\n");
        // handle cases when argc doesn't equal 2
        return 1;
    }
}