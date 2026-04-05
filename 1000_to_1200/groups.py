# cook your dish here
for _ in range(int(input())):
    s = input()
    
    count = 0
    for i in range(len(s)):
        if s[i] == "1" and (i == 0 or s[i - 1] == "0"):
            count += 1
            
    print(count)