# cook your dish here
for _ in range(int(input())):
    n = int(input())
    elements = input().split()

    counts = {}
    for element in elements:
        counts[element] = counts.get(element, 0) + 1

    print('YES' if all(count % 2 == 0 for count in counts.values()) else 'NO')