import unittest

def primePair(n):
    if n < 5:
        return 0
    primes = [2, 3]
    count = 0
    def isPrime(i):
        for p in primes:
            if i % p == 0:
                return
        primes.append(i)
    for i in range(5, n + 1):
        isPrime(i)
    for p, a in zip(primes, primes[1:]):
        if a - p == 2:
            count = count + 1
    return count

def primePair(n):
    flag = [1] * (n + 2)
    flag[0] = flag[1] = 0
    result = []

    for i in range(2,n + 1):
        if flag[i]:
            result.append(i)
            p = 2
            while i * p <= n:
                flag[i * p] = 0
                p += 1

    c = 0
    for i in range(len(result) - 1):
        if (result[i + 1] - result[i]) == 2:
            c += 1
    return c
class callatzTestCase(unittest.TestCase):
    def test_callatz(self):
        self.assertEqual(primePair(20), 4)

if __name__ == '__main__':
    unittest.main()