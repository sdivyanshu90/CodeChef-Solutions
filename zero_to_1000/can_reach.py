# Question Link: https://www.codechef.com/problems/CAN_REACH

# cook your dish here
for _ in range(int(input())):
    x, y, k = map(int, input().split())
    if x % k == 0 and y % k == 0:
        print("YES")
    else:
        print("NO")