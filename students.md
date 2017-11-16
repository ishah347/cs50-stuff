# Comparing Students

## Questions

1.1. It in itself serves as a pointer to a function that would be made by a coder before
using the qsort function that would compare two arguments that returns an integer, returning a negative integer value if the first argument is less than the
second one, a positive integer value if the first argument is greater than the second one, and zero if the arguments are equal, that has
parameters of type const void*.

1.2. While qsort was made to be able to sort any data type, which is why the function int (*comp)(const void *, const void *) points to
needs parameters of type void*, so that it can point to any data type, the example deals with integers. Thus, the compare function
seeks to compare two integer values, but to do so, one would have to retrieve the integer value the void pointers point to. However, since
the code's compiler isn't able to know what data type the void pointer is referencing, it is necessary for dereferencing purposes to
typecast from const void * to const int *.

1.3. See `students.c`.

1.4. See `students.py`.

1.5. See `students.js`.

## Debrief

a. Lecture 4 notes, http://www.circuitstoday.com/void-pointers-in-c, http://en.cppreference.com/w/c/algorithm/qsort, https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions,
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort

b. 120 minutes
