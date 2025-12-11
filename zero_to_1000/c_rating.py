# Question Link: https://www.codechef.com/problems/C_RATING

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    print((y - x + 7) // 8)