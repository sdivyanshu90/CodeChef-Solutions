# Question Link: https://www.codechef.com/problems/DOREWARD

# cook your dish here
for _ in range(int(input())):
    x = int(input())
    if x <= 3:
        print("BRONZE")
    elif x > 3 and x <= 6:
        print("SILVER")
    else:
        print("GOLD")