# Question Link: https://www.codechef.com/problems/EASYPERM

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    perm = list(range(n, 0, -1))
    print(*perm)