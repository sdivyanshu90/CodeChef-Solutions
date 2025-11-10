# Question Link: https://www.codechef.com/problems/TABLETS

# cook your dish here
for _ in range(int(input())):
    a, b = map(int, input().split())
    if 3 * a <= b:
        print("YES")
    else:
        print("NO")