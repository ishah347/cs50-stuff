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
        // Use argv[1] value as key
        string k = argv[1];
        for (int l = 0, n = strlen(k); l < n; l++)
        {
            // Differentiate between a valid entry and an invalid entry
            if (!(isalpha(k[l])))
            {
                printf("Usage: ./vigenere k\n");
                return 1;
            }
        }
        for (int i = 0, n = strlen(k); i < n; i++)
        {
            if (isalpha(k[i]))
            {
                // Set up "plaintext" prompt
                string pl;
                {
                    pl = get_string("plaintext: ");
                }
                // Set up "ciphertext" segment
                printf("ciphertext: ");
                for (int j = 0, m = strlen(pl); j < m; j++)
                {
                    // Ensure plaintext entry is alphabetical
                    if (isalpha(pl[j]))
                    {
                        // Differentiate between uppercase and lowercase key and plaintext entries in order to preserve case
                        if (isupper(pl[j]))
                        {
                            if (isupper(k[j % n]))
                            {
                                // Use key to instigate code
                                // Convert all values from ASCII to alphabetical for the use of equation, then the result to ASCII
                                char upup = ((pl[j] - 65) + (k[j % n] - 65)) % 26 + 65;
                                // Print the ciphertext
                                printf("%c", upup);
                            }
                            else if (islower(k[j % n]))
                            {
                                // Use key to instigate code
                                // Convert all values from ASCII to alphabetical for the use of equation, then the result to ASCII
                                char uplow = ((pl[j] - 65) + (k[j % n] - 97)) % 26 + 65;
                                // Print the ciphertext
                                printf("%c", uplow);
                            }
                        }
                        else if (islower(pl[j]))
                        {
                            if (isupper(k[j % n]))
                            {
                                // Use key to instigate code
                                // Convert all values from ASCII to alphabetical for the use of equation, then the result to ASCII
                                char lowup = ((pl[j] - 97) + (k[j % n] - 65)) % 26 + 97;
                                // Print the ciphertext
                                printf("%c", lowup);
                            }
                            else if (islower(k[j % n]))
                            {
                                // Use key to instigate code
                                // Convert all values from ASCII to alphabetical for the use of equation, then the result to ASCII
                                char lowlow = ((pl[j] - 97) + (k[j % n] - 97)) % 26 + 97;
                                // Print the ciphertext
                                printf("%c", lowlow);
                            }
                        }
                    }
                    // If plaintext isn't alphabetical, simply repost it in ciphertext
                    else
                    {
                        printf("%c", pl[j]);
                    }
                }
                printf("\n");
                return 0;
            }
        }
    }
    else
    {
        // handle cases when argc doesn't equal 2
        printf("Usage: ./vigenere k\n");
        return 1;
    }
}