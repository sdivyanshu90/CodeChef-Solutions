# Question Link: https://www.codechef.com/problems/MAXCOUNT

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    max_freq = 0
    answer = float('inf')
    
    for num in freq:
        if freq[num] > max_freq:
            max_freq = freq[num]
            answer = num
        elif freq[num] == max_freq:
            answer = min(answer, num)
    
    print(answer, max_freq)