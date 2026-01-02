# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    boy, girl = 0, 0
    for i in range(n):
        if s[i] == "G":
            girl += 1
        else:
            boy += 1
        if 2*girl < boy:
            break
        
    print(boy + girl)