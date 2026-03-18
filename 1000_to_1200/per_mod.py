# cook your dish here
for _ in range(int(input())):
    n = int(input())
    out = []
    
    if n == 1:
        out.append("-1")
    else:
        perm = [str(i) for i in range(2, n+1)]
        perm.append("1")
        out.append(" ".join(perm))
    print(*out)