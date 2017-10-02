#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <cs50.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image\n");
        return 1;
    }
    // open memory file
    char *f = argv[1];
    FILE *file = fopen(f, "r");
    if (file == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", f);
        return 2;
    }
    // define infile, buffer, and filename
    FILE *img = NULL;
    BYTE buffer[512];
    char filename[8];
    // define n (if n == 0, a new jpg has been found) and m (the number of that specific jpg)
    int m = 0;
    int n = 0;
    // have program read memory file 512 bytes at a time while trying to extract the jpgs
    while (fread(buffer, 512, 1, file) == 1)
    {
        // if a header is found
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // if a new jpg has been found
            if (n == 0)
            {
                // print to infile
                sprintf(filename, "%03i.jpg", m);
                img = fopen(filename, "w");
                // ensure infile isn't empty and exists after having been printed to
                if (img == NULL)
                {
                    return 3;
                }
                // write to infile 512 bytes at a time
                fwrite(buffer, 512, 1, img);
                // Establish that a jpg has been found and increase the number for the next jpg
                m++;
                n++;
            }
            // if a new jpg hasn't been found
            else
            {
                // close infile as it currently stands
                fclose(img);
                // print to infile
                sprintf(filename, "%03i.jpg", m);
                img = fopen(filename, "w");
                // ensure infile isn't empty and exists after having been printed to
                if (img == NULL)
                {
                    return 3;
                }
                // write to infile 512 bytes at a time
                fwrite(buffer, 512, 1, img);
                // increase the number for the next jpg
                m++;
            }
        }
        // if header hasn't been found
        else
        {
            // if a new jpg hasn't been found
            if (n)
            {
                // write to infile 512 bytes at at time
                fwrite(buffer, 512, 1, img);
            }
        }
    }
    // close infile
    fclose(file);

    // close outfile
    fclose(img);

    // success
    return 0;
}