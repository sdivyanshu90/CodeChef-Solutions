# Question Link: https://www.codechef.com/problems/ASM120

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    while x != 0:
        x, y = y % x, x
    print(y)