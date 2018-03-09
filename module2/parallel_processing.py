import heapq


def process(n, processes):
    result = []
    processors = [(0, i) for i in range(n)]
    heapq.heapify(processors)
    for i in processes:
        time, number = heapq.heappop(processors)
        result.append((number, time))
        heapq.heappush(processors, (time + i, number))
    return result


def main():
    n, _ = map(int, input().split())
    processes = list(map(int, input().split()))
    result = process(n, processes)
    for i in result:
        print(i[0], i[1])


if __name__ == "__main__":
    main()
