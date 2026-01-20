# cook your dish here
for _ in range(int(input())):
    x, a, b = map(int, input().split())
    solb = a + (100 - x) * b
    print(10 * solb)