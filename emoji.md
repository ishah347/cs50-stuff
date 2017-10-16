# Emoji

## Questions

1. 2.5 bytes

2. One char is representative of just one byte, but since the jack-o-lantern emoji is represented by 2.5 bytes, it cannot be represented by a char.

3.

```c
emoji get_emoji(string prompt)
{
    prompt = get_string("Code point: ");
    int n = strlen(prompt);
    char *endptr = NULL;
    if (n <= 2)
    {
        fprintf(stderr, "Please use right format for hexadecimal input");
        return false;
    }
    if (prompt[0] != 'U' || prompt[1] != '+')
    {
        fprintf(stderr, "Please use right format for hexadecimal input");
        return false;
    }
    prompt[0] = '0';
    prompt[1] = 'x';
    for (int i = 2; i < n; i++)
    {
        if (!isdigit(prompt[i]))
        {
            if (!isalpha(prompt[i]))
            {
                fprintf(stderr, "Please use right format for hexadecimal input");
                return false;
            }
            if (tolower(prompt[i]) > 'f')
            {
                fprintf(stderr, "Please use right format for hexadecimal input");
                return false;
            }
        }
    }
    long int converted = strtol(prompt, &endptr, 16);
    return converted;
}
```

## Debrief

1. CS50 Reference

2. 3 hours
