# cook your dish here
for _ in range(int(input())):
    s = input()
    t = input()
    res = ""
    for i in range(5):
        if s[i] == t[i]:
            res += "G"
        else:
            res += "B"
            
    print(res)