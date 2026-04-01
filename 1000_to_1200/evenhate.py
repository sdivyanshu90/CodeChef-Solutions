# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    even = sum(1 for x in a if x % 2 == 0)
    odd = n - even
    if odd == 0:
        print(0)
    else:
        print((odd // 2) + even + (odd % 2))