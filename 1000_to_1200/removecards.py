# cook your dish here
for _ in range(int(input())):
    n = int(input())
    cards = list(map(int, input().split()))
    freq = {}
    max_freq = 0
    
    for card in cards:
        freq[card] = freq.get(card, 0) + 1
        max_freq = max(max_freq, freq[card])
    
    moves = n - max_freq
    print(moves)