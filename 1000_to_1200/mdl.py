# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    while len(arr) >= 3:
        first_three = arr[:3]
        median = sorted(first_three)[1]
        arr.remove(median)
    
    print(*arr)