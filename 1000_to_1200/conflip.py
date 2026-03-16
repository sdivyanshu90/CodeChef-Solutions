# cook your dish here
for _ in range(int(input())):
    n = int(input())
    for _ in range(n):
        i, coins, q = map(int, input().split())
        
        if q == i:
            print(coins // 2)
        else:
            print(coins // 2 + coins % 2)