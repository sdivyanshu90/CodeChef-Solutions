# cook your dish here
for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    longest_streak = 1
    current_streak = 1
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            current_streak += 1
            longest_streak = max(longest_streak, current_streak)
        else:
            current_streak = 1
    
    max_streak = longest_streak
    
    for i in range(n):
        original_value = arr[i]
        arr[i] *= m
        
        longest_streak = 1
        current_streak = 1
        for j in range(1, len(arr)):
            if arr[j] >= arr[j - 1]:
                current_streak += 1
                longest_streak = max(longest_streak, current_streak)
            else:
                current_streak = 1
        
        max_streak = max(max_streak, longest_streak)
        arr[i] = original_value
    
    print(max_streak)