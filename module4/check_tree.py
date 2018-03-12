import sys


class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

    def check(self):
        correct = True
        if self.right != -1:
            correct = self.key <= self.right.min_key() and self.right.check()
        if correct and self.left != -1:
            correct = self.left.max_key() < self.key and self.left.check()
        return correct

    def max_key(self):
        cur = self
        while cur.right != -1:
            cur = cur.right
        return cur.key

    def min_key(self):
        cur = self
        while cur.left != -1:
            cur = cur.left
        return cur.key


def main():
    n = int(input())
    sys.setrecursionlimit(1000000000)
    nodes = []
    for i in range(n):
        key, left, right = map(int, input().split())
        nodes.append(Node(key, left, right))
    if nodes:
        tree = nodes[0]
        for i in nodes:
            if i.left != -1:
                i.left = nodes[i.left]
            if i.right != -1:
                i.right = nodes[i.right]

        print("CORRECT" if tree.check() else "INCORRECT")
    else:
        print("CORRECT")


if __name__ == "__main__":
    main()
