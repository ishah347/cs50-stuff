# Questions

## What's `stdint.h`?

stdint.h is a header in the C library that allows one to declare and define exact-width integer types, each with a minimum and a maximum, with the use of macros to make our code more transportable.

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

Using them makes it apparent that you intend to use the data, as each represent an integer of 8, 32, or 16 bits width.

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

BYTE is one byte, DWORD is four bytes, LONG is 4 bytes, and WORD is 2 bytes.

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

They, as a WORD, must specify that the file is a bitmap with the ASCII letters B and M (the hex 0x4D42).

## What's the difference between `bfSize` and `biSize`?

While bfSize is the size, in bytes, of the bitmap file, biSize is the number of bytes needed by the structure.

## What does it mean if `biHeight` is negative?

It indicates that there is a top-down DIB, which can't be compressed. biCompression in this case must be either BI_RGB or BI_BITFIELDS.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

fopen might not be able to find the file, so it might not exist.

## Why is the third argument to `fread` always `1` in our code?

Our program is reading just one RGB triple at a time.

## What value does line 65 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

A value of 3.

## What does `fseek` do?

It moves the process of the program to a specific place in the file.

## What is `SEEK_CUR`?

It means that, for the program, the offset is being counted from the current position in the file.
