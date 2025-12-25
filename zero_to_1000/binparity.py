# cook your dish here
for _ in range(int(input())):
    n = int(input())
    bits = bin(n)[2:]
    # print(bits)
    res = 0
    for bit in bits:
        res += int(bit)
    # print(res)
    if res % 2 == 0:
        print("EVEN")
    else:
        print("ODD")