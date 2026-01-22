# Question Link: https://www.codechef.com/problems/NOWINNER

# cook your dish here
for _ in range(int(input())):
    a, b, c, m = map(int, input().split())
    scores = sorted([a,b,c])
    a, b, c = scores[0], scores[1], scores[2]
    if (a + m >= b) or (b + m >= c):
        print("YES")
    else:
        print("NO")