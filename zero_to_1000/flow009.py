# cook your dish here
for _ in range(int(input())):
    quantity, price = map(int, input().split())
    tot = quantity * price
    if quantity > 1000:
        print(tot  - (0.1*tot))
    else:
        print(tot)