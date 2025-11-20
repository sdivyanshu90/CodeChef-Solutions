# Question Link: https://www.codechef.com/problems/WATERFLOW

# cook your dish here
for _ in range(int(input())):
    w, x, y, z = map(int, input().split())
    tot_buck = w + (y * z)
    if tot_buck == x:
        print("filled")
    elif tot_buck > x:
        print("overflow")
    else:
        print("Unfilled")