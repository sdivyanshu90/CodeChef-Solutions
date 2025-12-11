# Question Link: https://www.codechef.com/problems/FCTRL2

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] * i
        
    print(dp[n])