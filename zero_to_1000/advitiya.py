# Question Link: https://www.codechef.com/problems/ADVITIYA

# cook your dish here
for _ in range(int(input())):
    s = input()
    target = 'ADVITIYA'
    res = 0
    for i in range(8):
        if s[i] != target[i]:
            if ord(s[i]) < ord(target[i]):
                res += (ord(target[i]) - ord(s[i]))
            else:
                res += (26 - (ord(s[i]) - ord(target[i])))
    print(res)