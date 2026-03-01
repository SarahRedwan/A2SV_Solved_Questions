n, k = map(int, input().split())
a = list(map(int, input().split()))

freq = {}
l = 0
unique = 0
ans = 0

for r in range(n):
    if a[r] not in freq:
        freq[a[r]] = 0
    if freq[a[r]] == 0:
        unique += 1
    freq[a[r]] += 1

    while unique > k:
        freq[a[l]] -= 1
        if freq[a[l]] == 0:
            unique -= 1
        l += 1

    ans += (r - l + 1)

print(ans)
