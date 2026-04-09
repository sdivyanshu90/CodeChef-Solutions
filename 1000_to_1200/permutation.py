# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = sorted(map(int, input().split()))
    target = list(range(1, n + 1))
    
    total = 0
    valid = True
    for a, t in zip(arr, target):
        diff = t - a
        if diff >= 0:
            total += diff
        else:
            valid = False
            break
    
    print(total if valid else -1)