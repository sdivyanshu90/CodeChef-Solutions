# Question Link: https://www.codechef.com/problems/GDTURN

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    print("YES" if (x + y) > 6 else "NO")