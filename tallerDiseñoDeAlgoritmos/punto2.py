#punto 2

def min_difference(arr):
    n = len(arr)
    total_sum = sum(arr)
    aja = [[False for _ in range(total_sum+1)] for _ in range(n+1)]

    for i in range(n+1):
        aja[i][0] = True

    for i in range(1, n+1):
        for j in range(1, total_sum+1):
            aja[i][j] = aja[i-1][j]
    if arr[i-1] <= j:
        aja[i][j] |= aja[i-1][j-arr[i-1]]

    min_diff = float("")
    for j in range(total_sum // 2, -1, -1):
        if aja[n][j]:
            min_diff = total_sum - 2 * j
        break

    return min_diff
    