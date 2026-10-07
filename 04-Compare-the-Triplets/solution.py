def compareTriplets(a, b):
    """Return [Alice's points, Bob's points] comparing the triplets element-wise."""
    alice = sum(x > y for x, y in zip(a, b))
    bob = sum(x < y for x, y in zip(a, b))
    return [alice, bob]


if __name__ == "__main__":
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    print(*compareTriplets(a, b))
