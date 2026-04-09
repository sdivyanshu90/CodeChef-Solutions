# Question Link: https://www.codechef.com/problems/CHNUM

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    positives = [num for num in arr if num >= 0]
    negatives = [num for num in arr if num < 0]
    
    positive_sum = sum(positives)
    negative_sum = sum(negatives)
    positive_count = len(positives)
    negative_count = len(negatives)
    positive_squared = positive_sum ** 2
    negative_squared = negative_sum ** 2
    
    if negative_count == 0:
        print(positive_count, positive_count)
    elif positive_count == 0:
        print(negative_count, negative_count)
    elif positive_squared >= negative_squared:
        print(positive_count, negative_count)
    else:
        print(negative_count, positive_count)