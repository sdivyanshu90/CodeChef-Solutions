# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(set(map(int, input().split())))
    a.sort()
    print(a[-1] + a[-2])