# Question Link: https://www.codechef.com/problems/PLACE0110

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    if abs(x - y) <= 1:
        print(x + y)
    else:
        print(2 * max(x, y) - 1)