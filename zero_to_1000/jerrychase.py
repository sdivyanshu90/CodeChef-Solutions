# Question Link: https://www.codechef.com/problems/JERRYCHASE

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x >= y:
        print("NO")
    else:
        print("YES")