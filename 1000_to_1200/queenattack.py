# Question Link: https://www.codechef.com/problems/QUEENATTACK

# cook your dish here
for _ in range(int(input())):
    n, x, y = map(int, input().split())
    row = 2 * (n - 1)
    diagonal = (
        min(x - 1, y - 1) + 
        min(x - 1, n - y) + 
        min(n - x, y - 1) + 
        min(n - x, n - y)
    )
    print(row + diagonal)