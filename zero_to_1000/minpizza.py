# Question Link: https://www.codechef.com/problems/MINPIZZA

# cook your dish here
for _ in range(int(input())):
    n, x = map(int, input().split())
    tot_slices = n * x
    if tot_slices % 4 == 0:
        print(tot_slices // 4)
    else:
        print((tot_slices // 4) + 1)