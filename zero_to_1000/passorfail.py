# cook your dish here
for _ in range(int(input())):
    n, x, p = map(int, input().split())
    marks = 3 * x + ((n - x) * -1)
    if marks >= p:
        print("PASS")
    else:
        print("FAIL")