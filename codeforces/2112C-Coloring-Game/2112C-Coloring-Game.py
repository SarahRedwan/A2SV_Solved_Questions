def solve():
    import sys
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        ans = 0
        mx = a[-1]

        for k in range(2, n):
            need = max(a[k], mx - a[k])
            i, j = 0, k - 1

            while i < j:
                if a[i] + a[j] > need:
                    ans += (j - i)
                    j -= 1
                else:
                    i += 1

        print(ans)
solve()