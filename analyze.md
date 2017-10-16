# Analyze This

## Questions

1a. Yes

1b. The upper bound is O(1), because no matter the number of elements in the list, the amount of steps performed in the algorithm is constant, 2.

2a. Yes

2b. The upper bound is O(n^2), because despite the alteration to the traditional bubble sort. The list begins with n elements, and as the list is iterated over n times, the amount of comparisons made will decrease from (n - 1) to (n - 2) to (n - 3) and so on, until the total amount is (n^2 - n)/2, which is approximately n^2.

3a. Yes

3b. The upper bound is O(n), where n is at most 52, since there are 52 possible cards (elements) in a deck. The algorithm goes through one card at a time in a manner that, in the end, despite the shuffling, is still linear and depends on the number of elements, so that the longest the running time could go for is if the deck contains all 52 cards and the queen of harts ends up being the last card found.

## Debrief

1. Lecture 3 notes

2. 2 hours
