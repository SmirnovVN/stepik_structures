import sys


def main():
    n = int(next(sys.stdin))
    book = {}
    for i in range(n):
        command = next(sys.stdin)
        if command.startswith('add'):
            _, number, name = command.split()
            book[number] = name
        elif command.startswith('find'):
            _, number = command.split()
            if number in book:
                print(book[number])
            else:
                print('not found')
        elif command.startswith('del'):
            _, number = command.split()
            if number in book:
                del book[number]


if __name__ == "__main__":
    main()
