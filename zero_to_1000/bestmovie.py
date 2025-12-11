# Question Link: https://www.codechef.com/problems/BESTMOVIE

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    score = []
    for i in range(n):
        a, b = map(int, input().split())
        score.append((a, b))
        
    # print(f"Score: {score}")
    res = []
    for i, j in score:
        if i >= 7:
            res.append((i, j))

    # print(f"Res: {res}")
    res.sort(key=lambda x: x[1])
    # print(f"Sorted Res: {res}")
    
    if res:
        print(res[0][1])
    else:
        print(-1)