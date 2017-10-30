import cs50
import sys


def main():
    # Return an error message and exit if length of sys.argv isn't 2 or if key is negative
    if len(sys.argv) != 2:
        print('Usage: python caesar.py key')
        sys.exit(1)
    key = int(sys.argv[1])
    if key < 0:
        print('Key needs to be a non-negative integer')
        sys.exit(2)
    # Prompt user for plaintext
    plaintext = cs50.get_string('plaintext: ')
    # Print ciphertext
    print('ciphertext: ', end='')
    for i in plaintext:
        # Only use key on alphabetical characters
        if i.isalpha():
            # Maintain uppercase/lowercase form for letters and apply key
            # Print results
            if i.isupper():
                print(chr(((ord(i) - ord('A') + key) % 26) + ord('A')), end='')
            if i.islower():
                print(chr(((ord(i) - ord('a') + key) % 26) + ord('a')), end='')
        else:
            print(i, end='')
    print()


if __name__ == '__main__':
    main()
