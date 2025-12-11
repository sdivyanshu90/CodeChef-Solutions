# Question Link: https://www.codechef.com/problems/DNASTRAND

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    res = ""
    for char in s:
        if char == "A":
            res += "T"
        elif char == "T":
            res += "A"
        elif char == "C":
            res += "G"
        else:
            res += "C"
    print(res)