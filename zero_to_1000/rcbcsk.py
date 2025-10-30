# Question Link: https://www.codechef.com/problems/RCBCSK

# cook your dish here
x, y = map(int, input().split())
if x - y > 17:
    print("RCB")
else:
    print("CSK")