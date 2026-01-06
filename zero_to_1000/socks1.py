# Question Link: https://www.codechef.com/problems/SOCKS1

# cook your dish here
a, b, c = map(int, input().split())
if a == b or b == c or a == c:
    print("YES")
else:
    print("NO")