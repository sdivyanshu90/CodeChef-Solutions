# Question Link: https://www.codechef.com/problems/TRISQ

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    if n < 4:
        print(0)
    else:
        m = (n - 4) // 2
        print(((m + 1)*(m + 2)) // 2)