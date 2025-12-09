# Question Link: https://www.codechef.com/problems/FINDSHOES

# cook your dish here
for _ in range(int(input())):
    n, left = map(int, input().split())
    if n < left:
        print(n)
    else:
        tot = n * 2
        right = tot - left
        print(right)