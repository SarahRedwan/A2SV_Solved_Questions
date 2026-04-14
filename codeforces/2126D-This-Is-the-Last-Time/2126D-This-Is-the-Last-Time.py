import heapq
    heap = []

    while True:
        while i < n and casinos[i][0] <= k:
            l, r, real = casinos[i]
            if k <= r:
                heapq.heappush(heap, -real)  # max heap
            i += 1

        if not heap:
            break

        best = -heapq.heappop(heap)

        if best <= k:
            break

        k = best

    print(k)