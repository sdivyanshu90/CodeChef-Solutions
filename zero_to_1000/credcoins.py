# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    tot_cred_coins = x * y
    print(tot_cred_coins // 100)