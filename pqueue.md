# Now Boarding

## Questions

1.

```c
typedef struct
{
    int array[CAPACITY];
    unsigned int group;
    int size;

}
pqueue;
```

2.  // Take a pointer to the queue to allow you to alter its contents.
    // Take a passenger, who is to be added to the queue.
    // Add that passenger to the end of the queue.
    // Increase the size of the queue by 1 to allow for another passenger to be added.
    // If there is another passenger to be added
        // return to beginning of enqueue function
    // Else
        // stop

3. The upper bound is O(n). The algorithm goes through one passenger at a time in a manner that is linear and depends on the number of elements.

4.  // Take a pointer to the queue to allow you to alter its contents.
    // Locate and remove a passenger of highest priority in queue.
    // Decrease the size of the queue by 1.
    // Return the passenger that was removed from the queue.
    // If there is at least one other passenger to be returned
        // If a passenger of equal priority exists
            // Repeat from the top with said passenger
        // Else
            // Repeat from the top with a passenger of one less priority
    // Else
        //stop

5. The upper bound is O(n^2). The list begins with n passengers, or elements, and as the list is iterated over n times, the amount of comparisons made will decrease from (n - 1) to (n - 2) to (n - 3) and so on, until the total amount is (n^2 - n)/2, which is approximately n^2.

## Debrief

1. Queues powerpoint from section, Lecture 5 notes

2. 1 hour
