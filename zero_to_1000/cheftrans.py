# Question Link: https://www.codechef.com/problems/CHEFTRANS

# cook your dish here
for _ in range(int(input())):
    x, y, z = map(int, input().split())
    if x + y < z:
        print("PLANEBUS")
    elif x + y > z:
        print("TRAIN")
    else:
        print("EQUAL")