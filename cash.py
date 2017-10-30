import cs50


def main():
    # Prompt user for float value for change until nonnegative value is given
    while True:
        change = cs50.get_float('Change owed: ')
        if change > 0:
            break

    # Convert to integer
    cents = round(change * 100)
    coins = 0
    # Go through each type of coin, adding to counter along the way
    coins += cents // 25
    cents = cents % 25
    coins += cents // 10
    cents = cents % 10
    coins += cents // 5
    cents = cents % 5
    coins += cents
    # Print counter
    print(coins)


if __name__ == '__main__':
    main()
