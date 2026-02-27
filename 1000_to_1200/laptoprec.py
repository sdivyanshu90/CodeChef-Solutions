# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    freq = {}
    for num in a:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
            
    maxi = max(freq.values())
    res = 0
    count = 0
    for key, val in freq.items():
        if val == maxi:
            count += 1
            res = key
            
    if count > 1:
        print("CONFUSED")
    else:
        print(res)