# Question Link: https://www.codechef.com/problems/CHEFCAND

# cook your dish here
for _ in range(int(input())):
    n, x = map(int, input().split())
    if n > x:
        rem = (n - x)
        if rem % 4 == 0:
            print(rem // 4)
        else:
            print(rem // 4 + 1)
    else:
        print(0)