# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
            
    flag = True
    # print(freq)
    for _, val in freq.items():
        
        if val % 2 == 0:
            continue
        else:
            flag = False
            
    if flag:
        print("YES")
    else:
        print("NO")