# Question Link: https://www.codechef.com/problems/WGHTS

# cook your dish here
for _ in range(int(input())):
    n, x, y, z = map(int, input().split())
    if n == x or n == y or n == z or n == (x + y) or n == (y + z) or n == (x + z) or n == (x + y + z):
        print("YES")
    else:
        print("NO")