# cook your dish here
for _ in range(int(input())):
    s = input().strip()
    
    up = 0
    down = 0
    
    for i in range(len(s)):
        if i == 0 or s[i] != s[i-1]:
            if s[i] == 'U':
                up += 1
            else:
                down += 1
    
    print(min(up, down))