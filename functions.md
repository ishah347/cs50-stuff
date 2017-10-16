# #functions

## Questions

1. This hash function categorizes the input into 26 categories by depending on the first letter of each alphabetical string in the input. It's possible that the input is so large though that categorizing it into just 26 categories might still lead to a lot of time needed to move down and through the hash table in each category, with many collisions happening. It's also possible that the majority of the alphabetical strings in the input begin with the same letter, which would render the hash function very insignificant and the running time almost linear.

2. The function is perfect in that it converts input into a range of distinct outputs without any collisions, since every combination of characters would produce a unique decimal integer due to the nature of the characters and how the bits make them up, thus preventing collisions from happening. However, in practice, C doesn't have the capabilities to hold the amount of memory and data such a large hash function would require.

3. The data space in the JPEGs is aleady being largely used to make and display the images. With such a small data size left, storing the 50 hashes in them would likely lead to frequent collisions.

4. A trie is considered to have running time of O(1) because its system of looking up and finding words using the letters in them is not in any way influenced by the amount of other words in the trie. A hashtable, however, can be influenced by the amount of other words in the hashtable, as demonstrated through the collisions that usually result during the hashing process. Additionally, in a worst case scenario, all of the input will be hashed by a hash function into the same category, at which point the algorithm becomes linear.

## Debrief

1. Lecture 5 notes, Wikipedia - Hash functions

2. 3 hours
