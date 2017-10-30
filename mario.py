import cs50


def main():
    # Prompt user for height until a value between 0 and 23 is given
    while True:
        m = cs50.get_int('height: ')
        if m >= 0 and m <= 23:
            break

    # Print spaces and hashtags so that pyramid begins with two hashes and increases toward the bottom
    for i in range(m):
        print(' ' * (m - 1 - i), end='')
        print('#' * (i + 2))


if __name__ == '__main__':
    main()
