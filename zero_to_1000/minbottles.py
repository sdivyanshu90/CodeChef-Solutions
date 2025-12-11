# Question Link: https://www.codechef.com/problems/MINBOTTLES

# cook your dish here
for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print((sum(a) + x - 1) // x)