# Question Link: https://www.codechef.com/problems/UTMOPR

# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = map(int, input().split())
    print('odd' if k == 1 else 'even')