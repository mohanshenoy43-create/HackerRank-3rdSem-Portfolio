from collections import Counter


def matchingStrings(strings, queries):
    """For each query, count how many times it occurs in strings."""
    freq = Counter(strings)
    return [freq[q] for q in queries]


if __name__ == "__main__":
    n = int(input())
    strings = [input().strip() for _ in range(n)]
    q = int(input())
    queries = [input().strip() for _ in range(q)]
    print(*matchingStrings(strings, queries), sep="\n")
