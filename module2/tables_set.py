import sys


def main():
    next(sys.stdin)
    tables = list(map(int, next(sys.stdin).split()))
    parent = [i for i in range(len(tables))]

    def find(i):
        if i != parent[i]:
            parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        i_id, j_id = find(i), find(j)
        if i_id == j_id:
            return i_id
        if tables[i_id] > tables[j_id]:
            parent[j_id] = i_id
            tables[i_id] += tables[j_id]
            return i_id
        else:
            parent[i_id] = j_id
            tables[j_id] += tables[i_id]
            return j_id

    maximal = max(tables)
    for line in sys.stdin:
        destination, source = map(int, line.split())
        maximal = max(tables[union(destination - 1, source - 1)], maximal)
        print(maximal)


if __name__ == "__main__":
    main()
