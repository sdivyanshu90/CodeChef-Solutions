# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    pos = 0
    neg = 0
    
    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
            
    total_pos = (pos * (pos - 1)) // 2
    total_neg = (neg * (neg - 1)) // 2
    
    print(total_neg + total_pos)