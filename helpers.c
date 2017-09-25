// Helper functions for music

#include <cs50.h>
#include <math.h>
#include "helpers.h"
#include <string.h>
#include <stdio.h>

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    // Separate the first term (numerator) and third term (denominator) of the fraction; convert from ASCII to standard numbers
    float x = fraction[0] - 48;
    float y = fraction[2] - 48;
    // Calculate number of eighths and return it
    int eighth = round(x / y * 8);
    return eighth;
}
// Calculates frequency (in Hz) of a note
int frequency(string note)
{
    // Account for when there's a #
    //Differentiate between when note[0] is A through B and C through G
    if (note[1] == 35)
    {
        if (note[0] <= 66)
        {
            float o = (note[0] - 64) + (12 * (note[2] - 52));
            o = pow(2, (o / 12)) * 440;
            int O = round(o);
            return O;
        }
        else
        {
            float p = (66 - note[0]) + (12 * (note[2] - 52));
            p = pow(2, (p / 12)) * 440;
            int P = round(p);
            return P;
        }
    }
    // Account for when there's a b
    //Differentiate between when note[0] is A through B and C through G
    if (note[1] == 98)
    {
        if (note[0] <= 66)
        {
            float q = (note[0] - 66) + (12 * (note[2] - 52));
            q = pow(2, (q / 12)) * 440;
            int Q = round(q);
            return Q;
        }
        else
        {
            float r = (64 - note[0]) + (12 * (note[2] - 52));
            r = pow(2, (r / 12)) * 440;
            int R = round(r);
            return R;
        }
    }
    // Account for when note[1] is a number
    //Differentiate between when note[0] is A through B and C through G
    else
    {
        if (note[0] <= 66)
        {
            float n = note[0] + (12 * (note[1] - 52)) - 65;
            n = pow(2, (n / 12)) * 440;
            int N = round(n);
            return N;
        }
        else
        {
            float m = 65 + 12 * ((note[1] - 52)) - note[0];
            m = pow(2, (m / 12)) * 440;
            int M = round(m);
            return M;
        }
    }
}
// Determines whether a string represents a rest
bool is_rest(string s)
{
    // Distinguish between rests (when string length is 0) and non-rests
    if (strlen(s) == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}