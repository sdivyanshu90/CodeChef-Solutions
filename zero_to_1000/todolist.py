# Question Link: https://www.codechef.com/problems/TODOLIST

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    d = list(map(int, input().split()))
    res = 0
    for num in d:
        if num >= 1000:
            res += 1
    print(res)