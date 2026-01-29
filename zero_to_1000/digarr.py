# Question Link: https://www.codechef.com/problems/DIGARR

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    zero, five = s.count('0'), s.count("5")
    if zero >= 1 or five >= 1:
        print("YES")
    else:
        print("No")