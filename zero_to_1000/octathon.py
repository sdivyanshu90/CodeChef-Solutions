# Question Link: https://www.codechef.com/problems/OCTATHON

# cook your dish here
x = int(input())
if x < 3:
    print("GOLD")
elif 3 <= x < 6:
    print("SILVER")
else:
    print("BRONZE")