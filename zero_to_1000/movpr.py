# Question Link: https://www.codechef.com/problems/MOVPR

# cook your dish here
x, y, z = map(int, input().split())
non_combo = 2 * x + 3 * y
combo = 2 * z + y
if non_combo > combo:
    print(combo)
else:
    print(non_combo)