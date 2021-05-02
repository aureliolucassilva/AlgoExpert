def nonConstructibleChange(coins):
    numberCoins = len(coins)

    # Simple
    if numberCoins == 0:
        return 1
    elif numberCoins == 1:
        if coins[0] != 1:
            return 1
        else:
            return 2
    elif numberCoins == 2:
        return sum(coins) + 1

    # Others
    orderCoins = sorted(coins)
    idx = 1
    smallestChange = orderCoins[0]
    while idx < numberCoins:
        if smallestChange + 1 >= orderCoins[idx]:
            someCoins = orderCoins[:idx]
            currentChange = sum(someCoins)
            smallestChange = currentChange + orderCoins[idx]
        idx = idx + 1

    return smallestChange + 1
