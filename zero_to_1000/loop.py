# cook your dish here
for _ in range(int(input())):
    a, b, m = map(int, input().split())
    a, b = min(a, b), max(a, b)
    dist1 = b - a
    dist2 = a + m - b
    print(min(dist1, dist2))