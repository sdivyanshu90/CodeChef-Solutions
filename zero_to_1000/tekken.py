# Question Link: https://www.codechef.com/problems/TEKKEN

# cook your dish here
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    maxi = max(a, b, c)
    if maxi == a:
        print("YES")
    else:
        print("NO")