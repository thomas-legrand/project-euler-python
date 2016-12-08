from functools import lru_cache

COINS = [1, 2, 5, 10, 20, 50, 100, 200]


@lru_cache(maxsize=1000)
def change(amount, coin_index):
    if amount < 0 or coin_index < 0:
        return 0
    if amount == 0:
        return 1
    return change(amount, coin_index - 1) + change(amount - COINS[coin_index], coin_index)


def run_test():
    assert change(3, 7) == 2


def main():
    # TODO: implement a DP solution for this problem
    run_test()
    print(change(200, 7))


if __name__ == '__main__':
    main()
