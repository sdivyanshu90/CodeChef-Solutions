# cook your dish here
for _ in range(int(input())):
    n, x, c = map(int, input().split())
    a = list(map(int, input().split()))
    tot = sum(a)
    for coins in a:
        profit = x - coins - c
        if profit > 0:
            tot += profit
    print(tot)