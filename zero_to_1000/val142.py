# Question Link: https://www.codechef.com/problems/VAL142

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    if n - 127 >= 0:
        print("YES")
    else:
        print("NO")