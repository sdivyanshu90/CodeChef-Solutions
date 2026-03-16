# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    max_sum = 0
    
    for i in range(n):
        for j in range(i+1, n):
            prod = arr[i] * arr[j]
            digit_sum = sum(map(int, str(prod)))
            max_sum = max(max_sum, digit_sum)
    
    print(max_sum)