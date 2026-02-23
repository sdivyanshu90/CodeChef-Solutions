# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    possible = False
    for count in freq.values():
        if count >= 2:
            possible = True
            break
    
    if possible:
        print(n - 2)
    else:
        print(-1)