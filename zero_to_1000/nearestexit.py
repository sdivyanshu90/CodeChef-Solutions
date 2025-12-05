# Question Link: https://www.codechef.com/problems/NEAREXIT

# cook your dish here
for _ in range(int(input())):
    x = int(input())
    left = x - 1
    right = 100 - x
    if left < right:
        print("LEFT")
    else:
        print("RIGHT")