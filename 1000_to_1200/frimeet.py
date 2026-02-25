# Question Link: https://www.codechef.com/problems/FRIMEET

# cook your dish here
for _ in range(int(input())):
    n, m = map(int, input().split())
    if n >= m:
        print("YES")
    else:
        print("NO")