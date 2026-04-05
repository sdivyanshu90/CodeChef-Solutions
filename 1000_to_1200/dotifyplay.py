# cook your dish here
for _ in range(int(input())):
    n, k, l = map(int, input().split())
    arr = []
    for _ in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))
        
    songs = []
    for t, lang in arr:
        if lang == l:
            songs.append(t)
          
    songs.sort(reverse = True)
  
    # print(songs)
    if len(songs) >= k:
        print(sum(songs[:k]))
    else:
        print(-1)