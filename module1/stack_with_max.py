import sys


class StackWithMax(list):
    def __init__(self):
        super().__init__()
        self.max_stack = []

    def push(self, value):
        if value >= self.max():
            self.max_stack.append(value)
        super().append(value)

    def pop(self, index=None):
        value = super().pop(-1)
        if value == self.max():
            del self.max_stack[-1]
        return value

    def max(self):
        if self.max_stack:
            return self.max_stack[-1]
        else:
            return 0


def main():
    _ = input()
    stack = StackWithMax()
    for command in sys.stdin:
        if command.startswith('push'):
            _, m = command.split()
            stack.push(int(m))
        elif command.startswith('pop'):
            stack.pop()
        elif command.startswith('max'):
            print(stack.max())


if __name__ == "__main__":
    main()
