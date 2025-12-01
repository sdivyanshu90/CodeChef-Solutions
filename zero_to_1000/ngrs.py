# Question Link: https://www.codechef.com/problems/NGRS

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x < 50:
        print("Z")
    elif y < 50 and x >= 50:
        print("F")
    else:
        print("A")