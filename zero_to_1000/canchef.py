# Question Link: https://www.codechef.com/problems/CANCHEF

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    mil = x * 15
    tot_dist = 2 * y
    if mil >= tot_dist:
        print("YES")
    else:
        print("NO")