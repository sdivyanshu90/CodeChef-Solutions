# Question Link: https://www.codechef.com/problems/BOWLBALL

# cook your dish here
for _ in range(int(input())):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    res = 0
    for i in range(len(a)):
        if x <= a[i] <= y:
            res += 1
            
    print(res)