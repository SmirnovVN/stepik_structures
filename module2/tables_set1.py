import sys


def process(tables, destination, source):
    parent = [i for i in range(len(tables))]

    def find(i):
        if i != parent[i]:
            parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        i_id, j_id = find(i), find(j)
        if i_id == j_id:
            return
        if tables[i_id] > tables[j_id]:
            parent[j_id] = i_id
            tables[i_id] += tables[j_id]
        else:
            parent[i_id] = j_id
            tables[j_id] += tables[i_id]

    union(destination - 1, source - 1)
    print(max(tables))


def main():
    next(sys.stdin)
    tables = list(map(int, next(sys.stdin).split()))
    for line in sys.stdin:
        destination, source = map(int, line.split())
        process(tables, destination, source)


if __name__ == "__main__":
    main()
