coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount: int, coin_set=coins) -> dict:
    """
    Жадібний алгоритм для визначення кількості монет.

    Повертає словник формату:
        {coin_value: coin_count, ...}
    Приклад:
        find_coins_greedy(113) -> {50: 2, 10: 1, 2: 1, 1: 1}
    """
    result = {}
    remaining = amount

    for coin in coin_set:
        if coin <= remaining:
            count = remaining // coin
            remaining -= count * coin
            result[coin] = count

        if remaining == 0:
            break

    # Прибираємо монети, яких 0
    return {k: v for k, v in result.items() if v > 0}

def find_min_coins(amount: int, coin_set=coins) -> dict:
    """
    Алгоритм динамічного програмування для визначення мінімальної кількості монет.

    Повертає словник формату:
        {coin_value: coin_count, ...}
    Приклад:
        find_min_coins(113) -> {50: 2, 10: 1, 2: 1, 1: 1}
    (Для даного набору монет збігається з результатом жадібного алгоритму,
     але загалом може відрізнятися, якщо набір монет інший.)
    """
    # dp[i] зберігає кортеж (мін_кількість_монет, словник_використаних_монет),
    # де мін_кількість_монет — це кількість монет, потрібна для формування суми i,
    # а словник_використаних_монет — це конкретний набір монет.
    dp = [(0, {})] + [(float('inf'), {}) for _ in range(amount)]

    for i in range(1, amount + 1):
        for coin in coin_set:
            if coin <= i:
                prev_count, prev_coins_dict = dp[i - coin]
                # Якщо використавши coin, отримаємо менше монет, ніж поточне dp[i][0], оновлюємо dp[i]
                if prev_count + 1 < dp[i][0]:
                    new_coins_dict = prev_coins_dict.copy()
                    new_coins_dict[coin] = new_coins_dict.get(coin, 0) + 1
                    dp[i] = (prev_count + 1, new_coins_dict)

    return dp[amount][1]

# ---- Приклад використання ----
if __name__ == "__main__":
    test_amounts = [99, 113]
    
    for amt in test_amounts:
        greedy_result = find_coins_greedy(amt)
        dp_result = find_min_coins(amt)
        print(f"Сума: {amt}")
        print(f"  Жадібний алгоритм: {greedy_result}")
        print(f"  Динамічне програмування: {dp_result}")
        print("-" * 40)
