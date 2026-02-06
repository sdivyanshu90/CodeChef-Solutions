# Question Link: https://www.codechef.com/problems/MOOCHEF

# cook your dish here
for _ in range(int(input())):
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    maxi, mini, happiness = 0, 0, 0
    for num in a:
        if l <= num and num <= r:
            happiness += 1
        else:
            happiness += -1
        maxi = max(maxi, happiness)
        mini = min(mini, happiness)
    print(maxi, mini)