row = col = 0

for i in range(5):
    arr = list(map(int, input().split()))
    for j in range(5):
        if arr[j] == 1:
            row = i + 1   
            col = j + 1

moves = abs(row - 3) + abs(col - 3)

print(moves)