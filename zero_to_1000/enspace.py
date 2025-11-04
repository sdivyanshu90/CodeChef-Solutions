# Question Link: https://www.codechef.com/problems/ENSPACE

# cook your dish here
for _ in range(int(input())):
    n, x, y = map(int, input().split())
    if x + 2 * y <= n:
        print("YES")
    else:
        print("NO")