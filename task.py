import timeit

coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount: int, coin_set=coins) -> dict:
    """
    Жадібний алгоритм для визначення кількості монет.

    Повертає словник формату:
        {coin_value: coin_count, ...}
    """
    result = {}
    for coin in coin_set:
        if amount >= coin:
            result[coin] = amount // coin
            amount %= coin
    return result

def find_min_coins(amount: int, coin_set=coins) -> dict:
    """
    Алгоритм динамічного програмування для визначення мінімальної кількості монет.

    Повертає словник формату:
        {coin_value: coin_count, ...}
    """
    min_coins = [0] + [float("inf")] * amount
    coin_count = [{} for _ in range(amount + 1)]

    for coin in coin_set:
        for x in range(coin, amount + 1):
            if min_coins[x - coin] + 1 < min_coins[x]:
                min_coins[x] = min_coins[x - coin] + 1
                coin_count[x] = coin_count[x - coin].copy()
                coin_count[x][coin] = coin_count[x].get(coin, 0) + 1

    return coin_count[amount]

if __name__ == "__main__":
    amounts = [10, 55, 113, 207, 505, 1001]
    results = []

    for amount in amounts:
        time_greedy = timeit.timeit(lambda: find_coins_greedy(amount), number=1000)
        time_dp = timeit.timeit(lambda: find_min_coins(amount), number=1000)
        results.append([amount, time_greedy, time_dp])

    print("Amount | Greedy Time (s) | DP Time (s)")
    for result in results:
        print(f"{result[0]:>6} | {result[1]:>14.8f} | {result[2]:>12.8f}")