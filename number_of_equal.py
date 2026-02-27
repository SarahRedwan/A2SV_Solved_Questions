n, t = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

count = 0
i = 0
j = 0

while i < n and j < t:
    if arr1[i] < arr2[j]:
        i += 1
    elif arr1[i] > arr2[j]:
        j += 1
    else:
        x = arr1[i]
        a1_count = 0
        a2_count = 0

        while i < n and arr1[i] == x:
            a1_count += 1
            i += 1

        while j < t and arr2[j] == x:
            a2_count += 1
            j += 1

        count += a1_count * a2_count

print(count)
