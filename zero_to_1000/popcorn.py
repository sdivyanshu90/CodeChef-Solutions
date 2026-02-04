# Question Link: https://www.codechef.com/problems/POPCORN

# cook your dish here
for _ in range(int(input())):
    a1, a2 = map(int, input().split())
    b1, b2 = map(int, input().split())
    c1, c2 = map(int, input().split())
    print(max(a1 + a2, b1 + b2, c1 + c2))