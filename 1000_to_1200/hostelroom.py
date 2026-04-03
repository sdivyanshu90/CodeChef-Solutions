# Question Link: https://www.codechef.com/problems/HOSTELROOM

# cook your dish here
for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    
    res = x
    for num in arr:
        x += num
        res = max(res, x)
    print(res)