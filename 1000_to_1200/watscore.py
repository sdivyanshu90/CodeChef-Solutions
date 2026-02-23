# cook your dish here
# cook your dish here
for _ in range(int(input())):
    n = int(input())
    
    max_scores = {}
    for _ in range(n):
        p, s = map(int, input().split())
        
        if p <= 8:
            if p in max_scores:
                max_scores[p] = max(max_scores[p], s)
            else:
                max_scores[p] = s
    
    print(sum(max_scores.values()))