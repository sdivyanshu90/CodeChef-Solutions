# Question Link: https://www.codechef.com/problems/VALIDMIN

# cook your dish here
for _ in range(int(input())):
    a = list(map(int, input().split()))
    if a.count(min(a)) >= 2:
        print("YES")
    else:
        print("NO")