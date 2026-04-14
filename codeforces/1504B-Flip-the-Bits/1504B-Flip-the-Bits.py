t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    a = input()

    zero_count = 0
    one_count = 0
    arr = []

    for i in range(n):
        if s[i] == "0":
            zero_count += 1
        else:
            one_count += 1

        arr.append([zero_count, one_count])

    flip =  0
    possible = True

    for i in range(n-1, -1, -1):

        if flip % 2 == 0:
            if s[i] != a[i]:
                if arr[i][0] != arr[i][1]:
                    possible = False
                    break
                else:
                    flip += 1
        else:
            if s[i] == a[i]:
                if arr[i][0] != arr[i][1]:
                    possible = False
                    break
                else:
                    flip += 1

    if possible:
        print("YES")
    else:
        print("NO")