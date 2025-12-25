# Question Link: https://www.codechef.com/problems/T20MCH

# cook your dish here
r, o, c = map(int, input().split())
times = (20 - o) * 6
scores = times * 6
if scores + c > r:
    print("YES")
else:
    print("NO")