# Question Link: https://www.codechef.com/problems/LONGQUEUE

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    pos = len(a) - 1
    while pos > 0 and a[pos - 1] <= a[pos] // 2:
        a.pop(pos - 1)
        pos -= 1
    print(pos + 1)