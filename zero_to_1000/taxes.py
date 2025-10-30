# Question Link: https://www.codechef.com/problems/TAXES

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    if n > 100:
        print(n - 10)
    else:
        print(n)