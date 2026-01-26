# Question Link: https://www.codechef.com/problems/ABNOMAT

# cook your dish here
for _ in range(int(input())):
    n, m = map(int, input().split())
    sa = set(input())
    sb = set(input())
    
    if len(sa | sb) == 26:
        print("NO")
    else:
        print("YES")