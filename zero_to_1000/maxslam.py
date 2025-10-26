# Question Link: https://www.codechef.com/problems/MAXSLAM

# cook your dish here
x = int(input())
tot = 25 - x
if tot % 4 == 0:
    print(tot // 4)
else:
    print(tot // 4 + 1)