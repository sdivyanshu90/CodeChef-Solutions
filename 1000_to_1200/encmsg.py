# Question Link: https://www.codechef.com/problems/ENCMSG

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    chars = list(s)

    for i in range(0, n - 1, 2):
        chars[i], chars[i + 1] = chars[i + 1], chars[i]
    
    for i in range(n):
        chars[i] = chr(ord('z') - (ord(chars[i]) - ord('a')))
    
    print(''.join(chars))