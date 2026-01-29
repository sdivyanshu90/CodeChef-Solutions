# Question Link: https://www.codechef.com/problems/BAKECAKE3

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    max_profit = 0

    for x in range(0, max(a) + 1):
        temp = 0
        for customers in a:
            temp += min(x, customers)
        profit = temp * 50 - x * n * 30
        max_profit = max(max_profit, profit)
    
    print(max_profit)