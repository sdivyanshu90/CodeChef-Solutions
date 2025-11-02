# Question Link: https://www.codechef.com/problems/RIGHTTHERE

# cook your dish here
for _ in range(int(input())):
    n, x = map(int, input().split())
    if n <= x:
        print("YES")
    else:
        print("NO")