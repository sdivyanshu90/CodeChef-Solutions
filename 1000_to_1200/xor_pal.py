# Question Link: https://www.codechef.com/problems/XOR_PAL

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    target = s[::-1]
    
    idx = []
    for i in range(len(s)):
        if s[i] != target[i]:
            idx.append(i + 1)
            
    print(idx)