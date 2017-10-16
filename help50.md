# Helping `help50`

## Questions

1. The modulo operation can only be used with operands that are integers, so try converting n from a float into an integer first.

2. "get_string" needs a prompt after it in parentheses in order to prompt the user for a line of text first that it can return as a string, or else the resulting string is simply void. Try "string input = get_string("Enter: ");" or use any other prompt phrase.

3. The value range of "char" is from -128 to 127, which the value of 0xff, 255, does not fit in. Try defining "buffer" as an unsigned char instead, whose value range is from 0 to 255.

4. Given that "NULL" is a single, scalar value (since it's a pointer type), and not a list of any kind, surrounding it in braces in this initialization is redundant. Try removing the braces surrounding "NULL".

## Debrief

1. CS50 Reference, "C - Data Types" on tutorialspoint.com, "aggregate initialization" and "scalar initialization" on cppreference.com

2. 1 hour
