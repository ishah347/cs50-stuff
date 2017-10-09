// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <cs50.h>
#include <strings.h>
#include <ctype.h>
#include <string.h>

#include "dictionary.h"

// Define node
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Create hash table
node *hashtable[27];

// Define number of words in dictionary
int numberofwords = 0;

// create hash function
int hash(char *str)
{
    if (isupper(str[0]))
    {
        return (str[0] - 65);
    }
    else if (islower(str[0]))
    {
        return (str[0] - 97);
    }
    return 39;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // convert const char *word to a normal char
    char lower[strlen(word) + 1];
    for (int j = 0; j < strlen(word); j++)
    {
        lower[j] = word[j];
    }

    // add null pointer to end of lower
    lower[strlen(word)] = '\0';

    // Hash lower, set cursor equal to the resulting value's spot in the hashtable
    node *cursor = hashtable[hash(lower)];

    // If there's a word in cursor, check if it exists in the dictionary; then check the next word, and so on, until there's no more words being inputted
    while (cursor != NULL)
    {
        if (strcasecmp(cursor -> word, lower) == 0)
        {
            return true;
        }
        cursor = cursor -> next;
    }
    return false;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Define word
    char word[LENGTH + 1];

    // Create memory file dictionary is loaded into
    FILE *memory = fopen(dictionary, "r");

    // Check if memory file is empty or doesn't exist
    if (memory == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", dictionary);
        return false;
    }

    // Read memory file word by word
    while (fscanf(memory, "%s", word) != EOF)
    {
        // Create space in memory to hold nodes
        node *node1 = malloc(sizeof(node));

        // Check if program ran out of memory
        if (node1 == NULL)
        {
            unload();
            return false;
        }

        // Set value to node1
        strcpy(node1 -> word, word);


        // Hash each word
        // if hashtable is empty at the resulting value, add node1 as value
        if (hashtable[hash(word)] == NULL)
        {
            hashtable[hash(word)] = node1;
            node1 -> next = NULL;
            numberofwords++;
        }
        else
        {
            node1 -> next = hashtable[hash(word)];
            hashtable[hash(word)] = node1;
            numberofwords++;
        }
    }

    // Close memory file
    fclose(memory);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return numberofwords;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // For each element of hashtable, if there is still memory there, free it before moving on to the next
    for (int k = 0; k < 27; k++)
    {
        node *cursor = hashtable[k];

        while (cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor -> next;
            free(temp);
        }
    }
    return true;
}