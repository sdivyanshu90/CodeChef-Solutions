# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    
    diff = float("inf")
    for i in range(1, n):
        diff = min(diff, abs(a[i] - a[i - 1]))
    
    print(diff)