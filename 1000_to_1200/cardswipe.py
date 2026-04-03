# cook your dish here
for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    max_count = 0
    swipes = {}
    for id in A:
        if id not in swipes:
            swipes[id] = 'in'
            count += 1
            max_count = max(max_count, count)
        else:
            if swipes[id] == 'in':
                swipes[id] = 'out'
                count -= 1
            else:
                swipes[id] = 'in'
                count += 1
                max_count = max(max_count, count)
    print(max_count)