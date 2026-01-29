# Question Link: https://www.codechef.com/problems/STOCKMARKET

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mini = min(a)
    print(sum(a) - mini)