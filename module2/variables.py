import sys


def main():
    n, e, d = map(int, next(sys.stdin).split())
    rank = [0]*n
    parent = [i for i in range(len(rank))]

    def find(i):
        if i != parent[i]:
            parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        i_id, j_id = find(i), find(j)
        if i_id == j_id:
            return
        if rank[i_id] > rank[j_id]:
            parent[j_id] = i_id
        else:
            parent[i_id] = j_id
            if rank[i_id] == rank[j_id]:
                rank[j_id] += 1

    for i in range(e):
        destination, source = map(int, next(sys.stdin).split())
        union(destination - 1, source - 1)

    for i in range(d):
        destination, source = map(int, next(sys.stdin).split())
        if find(destination - 1) == find(source - 1):
            print(0)
            return

    print(1)


if __name__ == "__main__":
    main()
