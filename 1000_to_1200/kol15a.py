# cook your dish here
for _ in range(int(input())):
    s = input()
    
    res = 0
    for char in s:
        if char.isdigit():
            res += int(char)
            
    print(res)