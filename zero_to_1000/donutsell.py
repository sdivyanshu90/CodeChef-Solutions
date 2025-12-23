# cook your dish here
for _ in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    sad_count = 0

    for cust in B:
        donut_type = cust - 1
        if A[donut_type] > 0:
            A[donut_type] -= 1
        else:
            sad_count += 1

    print(sad_count)