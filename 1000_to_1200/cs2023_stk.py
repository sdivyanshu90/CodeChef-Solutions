# Question Link: https://www.codechef.com/problems/CS2023_STK

# cook your dish here
for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    streak_count_a = 0
    streak_count_b = 0
    
    current_streak_a = 0
    for streak in A:
        if streak > 0:
            current_streak_a += 1
            streak_count_a = max(streak_count_a, current_streak_a)
        else:
            current_streak_a = 0
    
    
    current_streak_b = 0
    for streak in B:
        if streak > 0:
            current_streak_b += 1
            streak_count_b = max(streak_count_b, current_streak_b)
        else:
            current_streak_b = 0

    if streak_count_a > streak_count_b:
        print("Om")
    elif streak_count_a < streak_count_b:
        print("Addy")
    else:
        print("Draw")