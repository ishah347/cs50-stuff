# Fair and Balanced

## Questions

1. Yes

2. Yes

3.

```c
bool balanced(int array[], int n)
{
    n = get_int("Enter size of array: ");
    int sum1 = 0;
    int sum2 = 0;
    for (int i = 0; i < n; i++)
    {

        array[i] = get_int("Enter element of array: ");
    }
    for (int j = 0; j < n / 2; j++)
    {
        sum1 = sum1 + array[j];
    }
    for (int k = (n + 1) / 2; k < n; k++)
    {
        sum2 = sum2 + array[k];
    }
    if (sum1 == sum2)
    {
        printf("true\n");
        return true;
    }
        printf("false\n");
        return false;
}
```

## Debrief

1. CS50 Reference

2. 2 hours
