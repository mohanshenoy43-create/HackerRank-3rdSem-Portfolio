def diagonalDifference(arr):
    """Absolute difference between the primary and secondary diagonal sums."""
    n = len(arr)
    primary = secondary = 0
    for i in range(n):
        primary += arr[i][i]
        secondary += arr[i][n - 1 - i]
    return abs(primary - secondary)


if __name__ == "__main__":
    n = int(input().strip())
    arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
    print(diagonalDifference(arr))
