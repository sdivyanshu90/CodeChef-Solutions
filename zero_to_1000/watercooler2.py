# Question Link: https://www.codechef.com/problems/WATERCOOLER2

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == y:
        print(0)
    else:
        print((y - 1) // x)