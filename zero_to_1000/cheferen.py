# cook your dish here
for _ in range(int(input())):
    n, a, b = map(int, input().split())
    even_count = n // 2
    odd_count = n - even_count
    print(even_count * a + odd_count * b)