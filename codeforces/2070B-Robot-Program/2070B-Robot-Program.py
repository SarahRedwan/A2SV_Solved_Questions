# First time reaching 0
    first_hit = -1
    for i in range(1, n + 1):
        if x + pref[i] == 0:
            first_hit = i
            break

    if first_hit == -1 or first_hit > k:
        print(0)
        continue

    # Find cycle from 0
    cycle_len = -1
    for i in range(1, n + 1):
        if pref[i] == 0:
            cycle_len = i
            break

    if cycle_len == -1:
        print(1)
    else:
        print(1 + (k - first_hit) // cycle_len)