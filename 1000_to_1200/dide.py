# Question Link: https://www.codechef.com/problems/DIDE

# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    mapped = {
        1: 6,
        2: 5,
        3: 4
    }
    
    res = sum(a)
    gains = []
    
    for num in a:
        if num <= 3:
            gains.append(mapped[num] - num)
    gains.sort(reverse=True)
    res += sum(gains[:k])
    print(res)