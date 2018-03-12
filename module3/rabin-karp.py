import sys
from functools import lru_cache


def main():
    pattern = next(sys.stdin).strip()
    text = next(sys.stdin).strip()
    x = 263
    p = 1000000007
    n = len(pattern)
    hashes = []

    @lru_cache(maxsize=None)
    def x_powered(power):
        if power == 0:
            return 1
        if power == 1:
            return x
        else:
            return (x_powered(power - 1) * x) % p

    def h(string):
        res = 0
        for j, ch in enumerate(string):
            res += ((ord(ch) * x_powered(j)) % p)

        return res % p

    def h_next(prev_h, last_ch, string):
        return ((prev_h - ord(last_ch) * x_powered(n - 1)) * x + ord(string[0])) % p

    pattern_hash = h(pattern)
    hashes.append(h(text[-n:]))
    last_char = text[-1]
    for i in range(len(text) - n - 1, -1, -1):
        window = text[i:i + n]
        hashes.append(h_next(hashes[-1], last_char, window))
        last_char = window[-1]

    hashes.reverse()
    first_char = pattern[0]
    for i, h in enumerate(hashes):
        if pattern_hash == h and text[i] == first_char:
            if text[i:i + n] == pattern:
                sys.stdout.write(str(i) + ' ')


if __name__ == "__main__":
    main()
