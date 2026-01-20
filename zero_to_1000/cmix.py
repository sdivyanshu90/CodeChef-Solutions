# Question Link: https://www.codechef.com/problems/CMIX

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    spell = []
    vol = []
    for _ in range(n):
        a, v = map(int, input().split())
        spell.append(a)
        vol.append(v)
        
    # print(sorted(lis, key = lambda x: x[1]))
#       [[5, 5], [1, 10]]
#       [[10, 2], [6, 6], [4, 7], [8, 9]]
#       [[50, 5], [45, 35], [35, 45], [5, 50]]
    # print("---------------------------------")
    # print(sorted(lis, key = lambda x: x[0]))
    # [[1, 10], [5, 5]]
    # [[4, 7], [6, 6], [8, 9], [10, 2]]
    # [[5, 50], [35, 45], [45, 35], [50, 5]]
    res = []
    for i in range((n)):
        for j in range((n)):
            if i < j:
                res.append(spell[i]*vol[j] + spell[j]*vol[i])
    print(max(res))