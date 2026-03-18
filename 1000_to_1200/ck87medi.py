# Question Link: https://www.codechef.com/problems/CK87MEDI

# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = sorted(map(int, input().split()))
    
    arr.extend([max(arr) + 1] * k)
    print(arr[len(arr) // 2])