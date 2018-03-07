class QueueWithMax(list):
    def __init__(self):
        super().__init__()
        self.stack1 = []
        self.stack2 = []

    def push(self, value):
        maximal = max(value, self.stack1[-1][1]) if self.stack1 else value
        self.stack1.append((value, maximal))

    def pop(self, index=None):
        if not self.stack2:
            while self.stack1:
                value = self.stack1.pop(-1)[0]
                maximal = max(value, self.stack2[-1][1]) if self.stack2 else value
                self.stack2.append((value, maximal))
        return self.stack2.pop(-1)[0]

    def max(self):
        if not self.stack1 or not self.stack2:
            return self.stack1[-1][1] if self.stack1 else self.stack2[-1][1]
        else:
            return max(self.stack1[-1][1], self.stack2[-1][1])


def max_window(lst, m):
    result = []
    window = QueueWithMax()
    for i in range(m):
        window.push(lst[i])
    result.append(window.max())
    for i in range(m, len(lst)):
        window.pop()
        window.push(lst[i])
        result.append(window.max())

    return result


def main():
    _ = int(input())
    lst = list(map(int, input().split()))
    m = int(input())
    print(" ".join(list(map(str, max_window(lst, m)))))


if __name__ == "__main__":
    main()
