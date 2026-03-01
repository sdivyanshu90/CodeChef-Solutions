# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    minus = sum(a[:n // 2])
    plus = sum(a[n // 2:])
    # print(f"Minus: {minus}, Plus: {plus}")
    # print(plus)
    print(plus - minus)