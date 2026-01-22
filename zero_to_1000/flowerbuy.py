# cook your dish here
for _ in range(int(input())):
    target = int(input())
    comb = []
    
    for count_2 in range(target // 2 + 1):
        for count_3 in range(target // 3 + 1):
            total = 2 * count_2 + 3 * count_3
            if total == target:
                combination = [2] * count_2 + [3] * count_3
                comb.append(combination)
    
    res = []
    for combo in comb:
        # print(combo)
        temp = 0
        for num in combo:
            if num == 2:
                temp += 4
            else:
                temp += 5
                
        res.append(temp)
    
    # print(res)
    print(min(res))