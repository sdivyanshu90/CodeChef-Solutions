# Question Link: https://www.codechef.com/problems/SNAPE

# cook your dish here
for _ in range(int(input())):
    b, ls = map(int, input().split())
    mini = ((b ** 2) + (ls ** 2)) ** 0.5
    maxi = ((abs((b ** 2) - (ls ** 2))) ** 0.5)
    print(maxi, mini)