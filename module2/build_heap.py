def sift_down(lst, elem):
    result = []
    while True:
        left = 2 * elem + 1 if 2 * elem + 1 < len(lst) else elem
        right = 2 * elem + 2 if 2 * elem + 2 < len(lst) else elem
        min_elem = elem if lst[elem] < lst[left] else left
        min_elem = min_elem if lst[min_elem] < lst[right] else right
        if min_elem != elem:
            lst[elem], lst[min_elem] = lst[min_elem], lst[elem]
            result.append((elem, min_elem))
            elem = min_elem
        else:
            break
    return result


def build_heap(lst):
    result = []
    for i in range(len(lst)//2, -1, -1):
        result.extend(sift_down(lst, i))
    return result


def main():
    _ = int(input())
    lst = list(map(int, input().split()))
    result = build_heap(lst)
    print(len(result))
    for i in result:
        print(i[0], i[1])


if __name__ == "__main__":
    main()
