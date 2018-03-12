import sys
from functools import lru_cache


class HashMap:
    def __init__(self, p, x, m):
        self.map = {i: [] for i in range(m)}
        self.p = p
        self.x = x
        self.m = m

    @lru_cache(maxsize=None)
    def x_powered(self, power):
        if power == 0:
            return 1
        if power == 1:
            return self.x
        else:
            return self.x_powered(power - 1) * self.x

    def h(self, string):
        result = 0
        for i, ch in enumerate(string):
            result += ((ord(ch) * self.x_powered(i)) % self.p)
        return (result % self.p) % self.m

    def put(self, string):
        if not self.find(string):
            self.map[self.h(string)].insert(0, string)

    def find(self, string):
        for i in self.map[self.h(string)]:
            if string == i:
                return True
        return False

    def remove(self, string):
        lst = self.map[self.h(string)]
        for i, elem in enumerate(lst):
            if string == elem:
                del lst[i]
                return True
        return False

    def get_list(self, i):
        return self.map[i]


def main():
    m = int(next(sys.stdin))
    n = int(next(sys.stdin))
    hashmap = HashMap(1000000007, 263, m)
    for i in range(n):
        command = next(sys.stdin)
        if command.startswith('add'):
            _, string = command.split()
            hashmap.put(string)
        elif command.startswith('find'):
            _, string = command.split()
            if hashmap.find(string):
                print('yes')
            else:
                print('no')
        elif command.startswith('del'):
            _, string = command.split()
            hashmap.remove(string)
        elif command.startswith('check'):
            _, i = command.split()
            lst = hashmap.get_list(int(i))
            if lst:
                print(" ".join(lst))
            else:
                print()


if __name__ == "__main__":
    main()
