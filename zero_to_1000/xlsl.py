# cook your dish here
for _ in range(int(input())):
    a, b, c, sm, l, xl = map(int, input().split())
    s = 0

    if c <= xl:
        s += c
        c = xl - c
    else:
        s += xl
        b += (c - xl)
    
    if b <= l:
        s += b
        b = l - b
    else:
        s += l
        a += (b - l)

    print(s + min(a, sm))