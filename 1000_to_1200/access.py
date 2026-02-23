# cook your dish here
for _ in range(int(input())):
    n, x = map(int, input().split())
    s = input()
    res = 0
    flag = True
    
    for k in s:
        if k == "1":
            res = x
        elif res == 0:
            flag = False
            break
        else:
            res -= 1
                
    if flag:
        print("YES")
    else:
        print("NO")