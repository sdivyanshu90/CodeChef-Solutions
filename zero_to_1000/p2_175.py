# Question Link: https://www.codechef.com/problems/P2_175

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    if n == 1 or n == 3:
        print(1)
    elif n % 2 == 0:
        print(n // 2 + 1)
    else:
        print(n // 2)