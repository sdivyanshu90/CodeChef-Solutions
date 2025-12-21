# Question Link: https://www.codechef.com/problems/ACS

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    res = sum(divmod(n, 100))
    # print(res)
    if res <= 10:
        print(res)
    else:
        print(-1)