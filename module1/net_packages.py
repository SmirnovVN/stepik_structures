import random
import unittest
import queue


def handle(packages, size):
    result, buffer = [-1] * len(packages), queue.Queue()
    time, execution, package_counter = 0, 0, 0
    while packages or buffer.qsize() != 0:
        execution -= 1

        while execution <= 0 and buffer.qsize() != 0:
            executed = buffer.get()
            execution = executed[1]
            result[executed[0]] = time
        if packages and time < packages[0][0]:
            time += 1
            continue
        for i in packages:
            if i[0] == time:
                if execution <= 0:
                    result[package_counter] = time
                    execution = i[1]
                elif buffer.qsize() < size - 1:
                    buffer.put((package_counter, i[1]))
                package_counter += 1
        packages[:] = [x for x in packages if x[0] != time]

        time += 1
    return result


def handle2(packages, size):
    result, buffer = [-1] * len(packages), []
    if packages:
        time, execution, package_counter = packages[0][0], 0, 0
        while packages or buffer:
            execution = penalty = 0

            while execution <= 0 and buffer:
                executed = buffer.pop()
                execution = executed[1]
                result[executed[0]] = time
                if executed[1]:
                    penalty += 1
            if packages and time < packages[0][0] and not execution:
                time = packages[0][0]
                continue
            for i in packages:
                if i[0] <= time:
                    if execution <= 0 and i[0] == time and not buffer:
                        result[package_counter] = time
                        execution = i[1]
                        if i[1]:
                            penalty += 1
                    elif (len(buffer) < size - 1 - penalty and i[0] < time) or (len(buffer) < size - penalty
                                                                                and (i[0] == time)):
                        buffer.insert(0, (package_counter, i[1]))
                    package_counter += 1
            packages[:] = [x for x in packages if x[0] > time]

            time += execution
    return result


def main():
    size, n = map(int, input().split())
    packages = []
    for i in range(n):
        packages.append(tuple(map(int, input().split())))
    print("\n".join(map(str, handle(packages, size))))


class TestHandleRandomPackages(unittest.TestCase):
    def test_random(self):
        while True:
            packages = []
            i = 0
            while i < 300:
                delta = random.randint(0, 32)
                packages.append((i, random.randint(0, 32)))
                i += delta
            size = random.randint(0, 15)
            packages2 = packages.copy()
            print(size)
            print(packages)
            self.assertEqual(handle(packages, size), handle2(packages2, size))


class TestHandleGeneratedPackages(unittest.TestCase):
    def test_generated(self):
        packages = [(0, 28), (7, 30), (24, 23), (45, 19), (73, 19), (76, 13), (77, 0), (99, 16), (111, 24), (122, 11),
                    (122, 3), (144, 5), (171, 0), (177, 5), (187, 17), (215, 21), (216, 2), (248, 9),
                    (253, 0), (285, 24)]
        packages2 = packages.copy()
        size = 5
        self.assertEqual(handle(packages, size), handle2(packages2, size))

    def test_generated2(self):
        packages = [(0, 30), (5, 22), (9, 3), (30, 5), (59, 17), (86, 7), (95, 32), (116, 18), (127, 5), (137, 30),
                    (147, 3), (174, 19), (183, 30), (196, 15), (223, 30), (246, 17), (262, 28), (278, 21)]
        packages2 = packages.copy()
        size = 3
        self.assertEqual(handle(packages, size), handle2(packages2, size))


class TestHandlePackages(unittest.TestCase):
    def test_first(self):
        s = list(map(int, '''16 0 29 3 44 6 58 0 72 2 88 8 95 7 108 6 123 9 139 6 152 6 157 3 169 3 183 1 192 0 202 8 213 8
        229 3 232 3 236 3 239 4 247 8 251 2 267 7 275 7'''.split()))
        packages = list(zip(s[::2], s[1::2]))
        self.assertEqual(handle(packages, 1), list(map(int, '''16 29 44 58 72 88 -1 108 123 139 152 -1 169 183 192 202 213
        229 232 236 239 247 -1 267 275'''.split())))

    def test_second(self):
        s = list(map(int, '''6 23 15 44 24 28 25 15 33 7 47 41 58 25 65 5 70 14 79 8 93 43 103 11 110 25 123 27 138 40
        144 19 159 2 167 23 179 43 182 31 186 7 198 16 208 41 222 23 235 26'''.split()))
        packages = list(zip(s[::2], s[1::2]))
        self.assertEqual(handle(packages, 11), list(map(int, '''6 29 73 101 116 123 164 189 194 208 216 259 270 295 322
        362 -1 381 -1 -1 -1 404 420 461 484'''.split())))

    def test_third(self):
        s = list(map(int, '''10 37 20 45 29 24 31 17 38 43 49 30 59 12 72 28 82 45 91 10 107 46 113 4 128 16 139 1 149
        41 163 0 172 22 185 1 191 17 201 3 209 11 223 30 236 17 252 42 262 0'''.split()))
        packages = list(zip(s[::2], s[1::2]))
        self.assertEqual(handle(packages, 13), list(map(int, '''10 47 92 116 133 176 206 218 246 291 301 347 351 367 368
         409 409 431 -1 -1 432 443 -1 473 -1'''.split())))

    def test_fourth(self):
        s = list(map(int, '''5 11 10 14 25 17 41 22 54 36 70 13 81 8 90 12 103 21 115 38 124 18 138 15 142 13 155 31 168
         0 177 49 186 8 196 30 206 37 217 49 232 31 247 25 260 31 268 36 279 8'''.split()))
        packages = list(zip(s[::2], s[1::2]))
        self.assertEqual(handle(packages, 12), list(map(int, '''5 16 30 47 69 105 118 126 138 159 197 215 230 243 274
        274 323 331 361 398 447 478 503 534 570'''.split())))

    def test_fifth(self):
        s = list(map(int, '''11 45 26 22 38 24 42 49 48 39 59 3 67 1 76 5 84 30 89 37 99 12 111 6 125 33 132 20 147 16
        160 7 174 15 185 14 198 9 200 37 208 18 222 3 237 28 248 10 263 11'''.split()))
        packages = list(zip(s[::2], s[1::2]))
        self.assertEqual(handle(packages, 11), list(map(int, '''11 56 78 102 151 190 193 194 199 229 266 278 284 317 -1
        337 -1 -1 344 353 390 408 411 -1 -1'''.split())))


class TestHandlePackages2(unittest.TestCase):
    def test_first(self):
        s = list(map(int, '''16 0 29 3 44 6 58 0 72 2 88 8 95 7 108 6 123 9 139 6 152 6 157 3 169 3 183 1 192 0 202 8 213 8
        229 3 232 3 236 3 239 4 247 8 251 2 267 7 275 7'''.split()))
        packages = list(zip(s[::2], s[1::2]))
        self.assertEqual(handle2(packages, 1), list(map(int, '''16 29 44 58 72 88 -1 108 123 139 152 -1 169 183 192 202 213
        229 232 236 239 247 -1 267 275'''.split())))

    def test_second(self):
        s = list(map(int, '''6 23 15 44 24 28 25 15 33 7 47 41 58 25 65 5 70 14 79 8 93 43 103 11 110 25 123 27 138 40
        144 19 159 2 167 23 179 43 182 31 186 7 198 16 208 41 222 23 235 26'''.split()))
        packages = list(zip(s[::2], s[1::2]))
        self.assertEqual(handle2(packages, 11), list(map(int, '''6 29 73 101 116 123 164 189 194 208 216 259 270 295 322
        362 -1 381 -1 -1 -1 404 420 461 484'''.split())))

    def test_third(self):
        s = list(map(int, '''10 37 20 45 29 24 31 17 38 43 49 30 59 12 72 28 82 45 91 10 107 46 113 4 128 16 139 1 149
        41 163 0 172 22 185 1 191 17 201 3 209 11 223 30 236 17 252 42 262 0'''.split()))
        packages = list(zip(s[::2], s[1::2]))
        self.assertEqual(handle2(packages, 13), list(map(int, '''10 47 92 116 133 176 206 218 246 291 301 347 351 367 368
         409 409 431 -1 -1 432 443 -1 473 -1'''.split())))

    def test_fourth(self):
        s = list(map(int, '''5 11 10 14 25 17 41 22 54 36 70 13 81 8 90 12 103 21 115 38 124 18 138 15 142 13 155 31 168
         0 177 49 186 8 196 30 206 37 217 49 232 31 247 25 260 31 268 36 279 8'''.split()))
        packages = list(zip(s[::2], s[1::2]))
        self.assertEqual(handle2(packages, 12), list(map(int, '''5 16 30 47 69 105 118 126 138 159 197 215 230 243 274
        274 323 331 361 398 447 478 503 534 570'''.split())))

    def test_fifth(self):
        s = list(map(int, '''11 45 26 22 38 24 42 49 48 39 59 3 67 1 76 5 84 30 89 37 99 12 111 6 125 33 132 20 147 16
        160 7 174 15 185 14 198 9 200 37 208 18 222 3 237 28 248 10 263 11'''.split()))
        packages = list(zip(s[::2], s[1::2]))
        self.assertEqual(handle2(packages, 11), list(map(int, '''11 56 78 102 151 190 193 194 199 229 266 278 284 317 -1
        337 -1 -1 344 353 390 408 411 -1 -1'''.split())))

    def test_many_similar(self):
        s = list(map(int, '''0 21 10 35 10 12 21 13 35 11 35 14 51 49 59 33 59 43 67 42 80 14 93 45 93 38 100 8 101 31
        108 46 123 22 127 20 139 7 142 43 142 12 142 25 154 25 154 5 154 42'''.split()))
        packages = list(zip(s[::2], s[1::2]))
        self.assertEqual(handle2(packages, 7), list(map(int, '''0 21 56 68 81 92 106 155 188 -1 231 245 290 -1 -1 328
        -1 -1 -1 -1 -1 -1 -1 -1 -1'''.split())))

    def test_many_similar_single_buffer(self):
        s = list(map(int, '''15 23 24 44 39 43 48 15 56 6 56 8 56 29 56 28 56 4 56 17 68 44 75 22 75 34 84 46 84 21 84
        25 97 31 105 34 105 43 117 17 129 12 142 47 144 22 144 18 152 9'''.split()))
        packages = list(zip(s[::2], s[1::2]))
        self.assertEqual(handle2(packages, 1), list(map(int, '''15 -1 39 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 84 -1 -1 -1 -1 -1
         -1 -1 142 -1 -1 -1'''.split())))

    def test_size_2(self):
        s = list(map(int, '''0 0 0 0 0 0 1 0 1 0 1 1 1 2 1 3'''.split()))
        packages = list(zip(s[::2], s[1::2]))
        self.assertEqual(handle2(packages, 2), list(map(int, '''0 0 0 1 1 1 2 -1'''.split())))


if __name__ == "__main__":
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestHandleRandomPackages)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHandleGeneratedPackages)
    unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHandlePackages2)
    unittest.TextTestRunner(verbosity=2).run(suite)
    # main()
