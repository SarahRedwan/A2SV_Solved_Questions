t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    blocks = 1
    for i in range(1, n):
        if s[i] != s[i-1]:
            blocks += 1

    if s[0] != s[-1] and blocks < n:
        print(blocks + 1)
    else:
        print(blocks)