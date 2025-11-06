# Question Link: https://www.codechef.com/problems/RAINFALL1

# cook your dish here
for _ in range(int(input())):
    x = int(input())
    if x < 3:
        print("LIGHT")
    elif x >= 3 and x < 7:
        print("MODERATE")
    else:
        print("HEAVY")