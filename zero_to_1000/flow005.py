# cook your dish here
for _ in range(int(input())):
    n = int(input())
    notes = [100, 50, 10, 5, 2, 1]
    count = 0
    for note in notes:
        if n >= note:
            count += n // note
            n %= note
        if n == 0:
            break
    print(count)