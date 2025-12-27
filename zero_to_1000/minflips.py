# Question Link: https://www.codechef.com/problems/MINFLIPS

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    v = list(map(int, input().split()))
    cnt1 = sum(1 for i in range(n) if v[i] == 1)
    if n % 2 == 1:
        print(-1)
    elif cnt1 >= n // 2:
        print(cnt1 - n // 2)
    else:
        print(n // 2 - cnt1)