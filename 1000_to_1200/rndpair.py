# Question Link: https://www.codechef.com/problems/RNDPAIR

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    total = (n * (n - 1)) // 2
    
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
            
    values = sorted(freq.keys(), reverse=True)
    maxi = values[0]
    c1 = freq[maxi]
    
    if c1 >= 2:
        good_pairs = (c1 * (c1 - 1)) // 2
    else:
        second_maxi = values[1]
        c2 = freq[second_maxi]
        good_pairs = c1 * c2
        
    print(good_pairs / total)