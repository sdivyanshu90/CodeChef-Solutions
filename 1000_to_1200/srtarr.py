# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    
    count = 0
    for i in range(n - 1):
        if s[i] == '1' and s[i + 1] == '0':
            count += 1
    
    print(count)