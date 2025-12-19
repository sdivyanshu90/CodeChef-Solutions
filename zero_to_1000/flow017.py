# cook your dish here
for _ in range(int(input())):
    a = list(map(int, input().split()))
    # Approach 1
    # second, largest = float('-inf'), float('-inf')
    
    # for num in a:
    #     if num > largest:
    #         second = largest
    #         largest = num
            
    #     elif num > second and num != largest:
    #         second = num
            
    # print(second)
    
    # Approach 2: Heap
    import heapq
    second = heapq.nlargest(2, a)
    print(second[1])