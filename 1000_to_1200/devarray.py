# cook your dish here
n, q = map(int, input().split())
a = list(map(int, input().split()))
amin = min(a)
amax = max(a)
queries = [int(input()) for _ in range(q)]

for query in queries:
    print('Yes' if amin <= query <= amax else 'No')