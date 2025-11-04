# Question Link: https://www.codechef.com/problems/SUMM

# cook your dish here
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a + b == c:
        print("YES")
    else:
        print("NO")