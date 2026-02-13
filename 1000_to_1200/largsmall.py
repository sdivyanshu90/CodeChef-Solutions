# Question Link: https://www.codechef.com/problems/LARGSMALL

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    min_val = min(arr)
    max_val = max(arr)
    if max_val - min_val <= 1:
        print(0)
    else:
        print(max_val - min_val - 1)