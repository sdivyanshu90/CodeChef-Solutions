# Question Link: https://www.codechef.com/problems/POOK

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    if n > 3:
        print(n)
    else:
        if n > 1:
            print(n - 1)
        else:
            print(1)