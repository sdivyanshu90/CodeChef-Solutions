# Question Link: https://www.codechef.com/problems/SCALENE

# cook your dish here
for _ in range(int(input())):
    a = list(map(int, input().split()))
    if len(a) == len(set(a)):
        print("YES")
    else:
        print("NO")