# cook your dish here
for _ in range(int(input())):
    a1, a2, b1, b2 = map(int, input().split())
    net_expa = a1 - a2
    net_expb = b1 - b2
    tot = net_expa + net_expb
    if -tot > 0:
        print("YES")
    else:
        print("NO")