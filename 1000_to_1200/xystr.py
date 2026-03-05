# Question Link: https://www.codechef.com/problems/XYSTR

# cook your dish here
for _ in range(int(input())):
    s = input().strip()
    i = 0
    pairs = 0
    
    while i < len(s) - 1:
        if s[i] != s[i+1]:
            pairs += 1
            i += 2
        else:
            i += 1
            
    print(pairs)