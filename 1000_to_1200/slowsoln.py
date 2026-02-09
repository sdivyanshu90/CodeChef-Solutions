# cook your dish here
for _ in range(int(input())):
    maxt, maxn, sumn = map(int, input().split())
    t = 0
    for i in range(1, maxt + 1):
        if i * maxn <= sumn:
            t += 1
    # print(t)
    rem = 0
    if sumn % (t * maxn) != 0 and t != maxt:
        rem = sumn - (t * maxn)
    # print(f"t: {t}")
    res = 0
    for i in range(1, t + 1):
        res += (maxn ** 2)
    res += (rem ** 2)
    print(res)

# Approach 2
# cook your dish here
for _ in range(int(input())):
    maxt, maxn, sumn = map(int, input().split())
    t = min(maxt, sumn // maxn)
    rem = sumn - t * maxn if t < maxt else 0
    res = t * (maxn ** 2) + (rem ** 2)
    print(res)