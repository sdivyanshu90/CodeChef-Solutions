# Question Link: https://www.codechef.com/problems/ADVITIYA2

# cook your dish here
for _ in range(int(input())):
    a, b, c, d, e = map(int, input().split())
    score = a + b + c + d + e
    if score >= 4:
        print("YES")
    else:
        print("NO")