# cook your dish here
for _ in range(int(input())):
    na, nb, nc = map(int, input().split())
    if na > (nb + nc) or nb > (na + nc) or nc > (na + nb):
        print("YES")
    else:
        print("NO")