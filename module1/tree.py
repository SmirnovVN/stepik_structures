import sys

sys.setrecursionlimit(20000)


def height(tree, root):
    h = 1
    if tree[root]:
        for i in tree[root]:
            h = max(h, height(tree, i) + 1)
    return h


def main():
    _ = input()
    leafs = list(map(int, input().split()))
    tree = [None] * len(leafs)
    for c, v in enumerate(leafs):
        if v != -1:
            if not tree[v]:
                tree[v] = []
            tree[v].append(c)
    root = leafs.index(-1)
    print(height(tree, root))


if __name__ == "__main__":
    main()


class ExtendedStack(list):
    def sum(self):
        self.append(self.pop() + self.pop())

    def sub(self):
        self.append(self.pop() - self.pop())

    def mul(self):
        self.append(self.pop() * self.pop())

    def div(self):
        self.append(self.pop() // self.pop())
