# Question Link: https://www.codechef.com/problems/KITCHENSPICE

# cook your dish here
for _ in range(int(input())):
    x = int(input())
    if x  < 4:
        print("MILD")
    elif 4 <= x < 7:
        print("MEDIUM")
    else:
        print("HOT")