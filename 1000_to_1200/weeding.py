# cook your dish here
for _ in range(int(input())):
    no_weed, m_total_days, k_spray_kill_weed = map(int, input().split())
    a = list(map(int, input().split()))
    for i in a:
        if m_total_days - i + 1 < k_spray_kill_weed:
            print("NO")
            break
    else:
        print("YES")