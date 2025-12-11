# Question Link: https://www.codechef.com/problems/CHEFBOTTLE

# cook your dish here
for _ in range(int(input())):
    n, x, k = map(int, input().split())
    if x > k:
        print(0)
    else:
        can_fill = k // x
        if can_fill > n:
            print(n)
        else:
            print(can_fill)