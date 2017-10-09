# Questions

## What is pneumonoultramicroscopicsilicovolcanoconiosis?

According to http://www.dictionary.com/browse/pneumonoultramicroscopicsilicovolcanoconiosis, it is "an obscure term ostensibly referring to a lung disease caused by silica dust, sometimes cited as one of the longest words in the English language".

## According to its man page, what does `getrusage` do?

getrusage() returns resource usage measures for who, which can be RUSAGE_SELF, RUSAGE_CHILDREN, or RUSAGE_THREAD.

## Per that same man page, how many members are in a variable of type `struct rusage`?

16 members

## Why do you think we pass `before` and `after` by reference (instead of by value) to `calculate`, even though we're not changing their contents?

Passing structs, especially considerably large ones, by value can be slow, can take up a lt of memory, and can cause stack overflow.

## Explain as precisely as possible, in a paragraph or more, how `main` goes about reading words from a file. In other words, convince us that you indeed understand how that function's `for` loop works.

The use of "for (int c = fgetc(file); c != EOF; c = fgetc(file))" means that fgetc will get the next character from file and will keep going through file until the end of the file. Each character is then analyzed. If they are alphabetical characters or apostrophes, they are appended into a word unitl it reaches its maximum length. Words that are too long or contain numbers are consumed, and the process is then reset in preparation for the next word. If a full word is found, the word is ended and the counter for the amount of words is increased, The word is then checked to see if it is mispelled (with the time taken to check recorded). If it is, it is printed. The process then resets itself for the next word.

## Why do you think we used `fgetc` to read each word's characters one at a time rather than use `fscanf` with a format string like `"%s"` to read whole words at a time? Put another way, what problems might arise by relying on `fscanf` alone?

fscanf reads until spaces, so it will include punctuation and such as part of the words.

## Why do you think we declared the parameters for `check` and `load` as `const` (which means "constant")?

Constant pointers don't change the values they point towards, and since we don't want to cause changes to words and the dictionary, we use const char* word and const char* dictionary for check and load, respectively.





