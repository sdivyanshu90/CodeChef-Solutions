# cook your dish here
for _ in range(int(input())):
    s = input()
    log = [s[i:i+2] for i in range(0, len(s), 2)]
    # print(log)
    sums = 0
    for day in log:
        a = day.count("A")
        b = day.count("B")
        sums += abs(a - b)
    if sums == 0:
        print("yes")
    else:
        print("no")