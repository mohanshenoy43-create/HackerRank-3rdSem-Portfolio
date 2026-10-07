def dynamicArray(n, queries):
    """Process type 1 / type 2 queries on n sequences; return the answers of type 2 queries."""
    seqs = [[] for _ in range(n)]
    last_answer = 0
    answers = []
    for q, x, y in queries:
        idx = (x ^ last_answer) % n
        if q == 1:
            seqs[idx].append(y)
        else:
            seq = seqs[idx]
            last_answer = seq[y % len(seq)]
            answers.append(last_answer)
    return answers


if __name__ == "__main__":
    n, q = map(int, input().split())
    queries = [list(map(int, input().split())) for _ in range(q)]
    print(*dynamicArray(n, queries), sep="\n")
