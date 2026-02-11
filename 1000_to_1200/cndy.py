# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    freq = {}
    for num in a:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
            
    # print(freq)
    flag = True
    for key, val in freq.items():
        if val > 2:
            flag = False
            break
    if flag or len(set(a)) == len(a):
        print("Yes")
    else:
        print("No")