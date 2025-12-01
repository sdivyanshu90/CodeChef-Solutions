# Question Link: https://www.codechef.com/problems/EPISODES

# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    tot = n * k
    hour = tot // 60
    minu = tot - (hour * 60)
    print(hour, minu)