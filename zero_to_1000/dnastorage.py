# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    res = ""
    for i in range(0, len(s), 2):
        pair = s[i: i + 2]
        if pair == "00":
           res += "A"
        elif pair == "01":
            res += "T"
        elif pair == "10":
            res += "C"
        else:
            res += "G"
            
    print(res)