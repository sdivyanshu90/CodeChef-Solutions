# Question Link: https://www.codechef.com/problems/ADD13

# cook your dish here
for _ in range(int(input())):
    n, m = map(int, input().split())
    diff = m - n
    if diff % 2 != 0 or m < n or m > 3*n:
        print("NO")
    else:
        print("YES")