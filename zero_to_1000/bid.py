# cook your dish here
for _ in range(int(input())):
    n = int(input())
    attA = list(map(int, input().split()))
    defA = list(map(int, input().split()))
    attP = list(map(int, input().split()))
    defP = list(map(int, input().split()))
    
    if sum(attA) > sum(attP) and sum(defA) > sum(defP):
        print("A")
    elif sum(attA) < sum(attP) and sum(defA) < sum(defP):
        print("P")
    else:
        print("DRAW")