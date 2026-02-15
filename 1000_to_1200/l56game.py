# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 1:
        print(1)
    else:
        res = sum(1 for num in a if num % 2)
        print(res % 2 + 1)