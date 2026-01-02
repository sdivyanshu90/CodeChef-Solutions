# Question Link: https://www.codechef.com/problems/SUPCHEF

# cook your dish here
for _ in range(int(input())):
    n, m, k =  map(int, input().split())
    if n > (m * k):
        print("YES")
    else:
        print("NO")