from bisect import bisect_left

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b.sort()

    a[0]= min(a[0],b[0]-a[0])
    flag = True

    for i in range(1, n):
        index = bisect_left(b, a[i] + a[i-1])

        if index == m and a[i] < a[i-1]:
            flag = False
            break

        if index == m:
            continue

        if a[i] >= a[i-1]:
            a[i] = min(a[i], b[index] - a[i])
        else:
            a[i] = b[index] - a[i]

    print("YES" if flag else "NO")