# Question Link: https://www.codechef.com/problems/NODDSM

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    odd = 0
    for x in arr:
        if x % 2 == 1:
            odd += 1

    even = n - odd

    if odd % 2 == 0:
        print(min(even, odd // 2))
    else:
        print(even)