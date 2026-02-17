# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    max_occur = max(a.count(i) for i in a)
    print(n - max_occur)