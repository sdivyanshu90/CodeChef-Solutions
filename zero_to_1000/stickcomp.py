# Question Link: https://www.codechef.com/problems/STICKCOMP

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(a.index(max(a)) + 1)