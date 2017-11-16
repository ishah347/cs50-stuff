# To be or not to be

## ~~That is the question~~ These are the questions

4.1. 1000

4.2. A counter is initialized under the name of "score" with an initial value of 0. Each character in the string genes is iterated over;
if it is equivalent to the character of the same position in the target, the string "to be or not to be", the counter is increased by 1.
After all 18 characters are iterated over, the fitness of genes is calculated by dividing the score, converted into a float to allow for
the fitness to be a decimal value, over the length of the target, which is 18.

4.3. 0.05555555555555555

4.4. The edit distance between the string genes and "to be or not to be" is equivalent to (18 - score), as it is equivalent to the number of
insertions, deletions, or substitutions of characters needed to transform genes into "to be or not to be", and since genes and "to be or not to be" have
the same length, 18, only substitutions may be found, and since the number of substitutions is equivalent to the number of characters
the two strings don't have in common, it is equivalent to (18 - score), since score represents the amount of characters they do have in common.
Thus, the fitness of genes is calculated by dividing (18 - edit distance), which is equivalent to score, converted into a float to allow for
the fitness to be a decimal value, over the length of the target, which is 18.

4.5. Although the processes of selection and crossover aid in the transfer of good genes (i.e. ones that would aid in eventually forming "to be or not to be") from one generation to the next, there's the possibility of
certain genes required to form "to be or not to be" not being in the previous generation, and so, without
one or more of the genes in a segment of children coming out of left-field and differing from what gene(s) his/her parents should have given him/her,
with there being a possibility that the old gene is undesired and the new gene is the one desired to form the target, the target may never be reached.
To take this into account in the code, every gene of every child of the new population had a possibility of being "mutated", as they are in real life. Using the
random.random function to produce a float value in the range [0.0, 1.0), if for a character in string genes for each child the resulting value is below the declared mutationRate, 0.01,
that character, which was produced by the crossover between the "child"'s "parents", is replaced by another random character to simulate
a mutation rate of approximately 1% in the real world.

## Debrief

a. https://docs.python.org/2/library/random.html, https://stackoverflow.com/questions/2460177/edit-distance-in-python

b. 90 minutes
