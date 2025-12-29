# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(str, input().split()))
    s, l = 0, 0
    for cont in a:
        if cont == "START38":
            s += 1
        else:
            l += 1
    print(s, l)