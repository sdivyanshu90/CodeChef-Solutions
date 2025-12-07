# Question Link: https://www.codechef.com/problems/BRKSTICK

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    for i in range(len(a)):
        res += (a[i] - 1)
    print(res)

# Approach 2
# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(a) - n)