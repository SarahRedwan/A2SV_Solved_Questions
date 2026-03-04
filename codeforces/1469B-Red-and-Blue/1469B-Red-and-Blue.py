t = int(input())

for _ in range(t):
    # read red array
    n = int(input())
    r = list(map(int, input().split()))

    # read blue array
    m = int(input())
    b = list(map(int, input().split()))

    # max prefix sum for red
    cur = 0
    best_red = 0
    for x in r:
        cur += x
        best_red = max(best_red, cur)

    # max prefix sum for blue
    cur = 0
    best_blue = 0
    for x in b:
        cur += x
        best_blue = max(best_blue, cur)

    # final answer
    print(best_red + best_blue)