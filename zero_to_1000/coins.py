# cook your dish here
coin_values = {}

def calculate_max_dollars(coin):
    if coin == 0:
        return 0
    if coin not in coin_values:
        max_dollars = calculate_max_dollars(coin // 2) + calculate_max_dollars(coin // 3) + calculate_max_dollars(coin // 4)
        coin_values[coin] = max(coin, max_dollars)
    return coin_values[coin]

while True:
    try:
        coin = int(input())
        print(calculate_max_dollars(coin))
    except EOFError:
        break