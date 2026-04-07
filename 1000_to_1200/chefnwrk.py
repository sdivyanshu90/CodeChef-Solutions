# Question Link: https://www.codechef.com/problems/CHEFNWRK

# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    bxs = list(map(int, input().split()))

    if bxs[0] > k:
        print(-1)
        continue

    trips = 0
    current_weight = 0

    for i in range(n):
        if bxs[i] > k:
            print(-1)
            break
        elif current_weight + bxs[i] <= k:
            current_weight += bxs[i]
            if i == n - 1:
                trips += 1
        else:
            trips += 1
            current_weight = bxs[i]
            if i == n - 1:
                trips += 1
    else:
        print(trips)