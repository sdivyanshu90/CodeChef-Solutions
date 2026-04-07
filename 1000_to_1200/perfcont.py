# Question Link: https://www.codechef.com/problems/PERFCONT

# cook your dish here
for _ in range(int(input())):
    n, p = map(int, input().split())
    arr = list(map(int, input().split()))
        
    easy, hard = 0, 0
    half = p // 2
    tenth = p // 10
    for num in arr:
        if num >= half:
            easy += 1
        elif tenth >= num:
            hard += 1
            
    # print(easy, hard)
            
    if easy == 1 and hard == 2:
        print("yes")
    else:
        print("no")