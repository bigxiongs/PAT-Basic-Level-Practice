import unittest

class Solution:
    def continueCallatz(self, nums):
        memo = {0}
        key = set()
        def callatz(num):
            if num == 0:
                return
            if num % 2 == 0:
                yield num // 2
            else:
                yield (num * 3 + 1) // 2
        for num in nums:
            if num not in memo:
                key.add(num)
            for n in callatz(num):
                if n in key:
                    key.remove(n)
                    break
                else:
                    memo.add(n)
        key = list(key)
        key.sort(reverse=True)
        return key

class SolutionTestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(Solution().continueCallatz([3, 5, 6, 7, 8, 11]), [7, 6])

if __name__ == '__main__':
    unittest.main()