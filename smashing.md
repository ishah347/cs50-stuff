# Stack Smashing

## Questions

1. Stack canaries are randomly chosen integer values that are stationed just before a return address. Thus, if the canary value is overwritten, it indicates that a malicious source is attempting to overwrite the return address, thereby taking over the code, using stack buffer overflow. Thus, if the canary value is shown to be changed, a malicious source is detected.

2. They are similar to canaries as they are used in coal mines. Canaries were brought into mines to detect carbon monoxide; they, being sensitive, became sick because of carbon monoxide before humans would, thus allowing the miners to detect the threat and take precautions. This is similar to how stack canaries are used to indicate malicious sources.

3.  #include <string.h>
    #include <stdio.h>
    #include <cs50.h>

    int main(void)
    {
        char buffer[1];
        string over = get_string("ENTER: ");
        strcpy(buffer, over);
        printf("%s\n", buffer);
    }

## Debrief

1. YouTube - Stack Canary, Wikipedia - Stack buffer overflow, Wikipedia - Sentinel species

2. 30 minutes
