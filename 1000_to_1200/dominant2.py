# Question Link: https://www.codechef.com/problems/DOMINANT2

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    freq = {}
    
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
            
    count = []
    for key, val in freq.items():
        count.append(val)
        
    # print(count)
    
    maxi = max(count)
    count.remove(maxi)
    same = False
    for c in count:
        if c == maxi:
            same = True
            
    if same:
        print("NO")
    else:
        print("YES")