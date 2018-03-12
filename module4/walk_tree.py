class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

    def walk_in_order(self):
        acc = []
        if self.left != -1:
            acc.extend(self.left.walk_in_order())
        acc.append(self.key)
        if self.right != -1:
            acc.extend(self.right.walk_in_order())
        return acc

    def walk_pre_order(self):
        acc = [self.key]
        if self.left != -1:
            acc.extend(self.left.walk_pre_order())
        if self.right != -1:
            acc.extend(self.right.walk_pre_order())
        return acc

    def walk_post_order(self):
        acc = []
        if self.left != -1:
            acc.extend(self.left.walk_post_order())
        if self.right != -1:
            acc.extend(self.right.walk_post_order())
        acc.append(self.key)
        return acc


def main():
    n = int(input())
    nodes = []
    for i in range(n):
        key, left, right = map(int, input().split())
        nodes.append(Node(key, left, right))
    tree = nodes[0]
    for i in nodes:
        if i.left != -1:
            i.left = nodes[i.left]
        if i.right != -1:
            i.right = nodes[i.right]

    print(" ".join(map(str, tree.walk_in_order())))
    print(" ".join(map(str, tree.walk_pre_order())))
    print(" ".join(map(str, tree.walk_post_order())))


if __name__ == "__main__":
    main()
